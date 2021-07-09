# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import platform
import socket
import subprocess
import webbrowser

from six.moves.urllib_parse import urlparse

from azure.core.exceptions import ClientAuthenticationError

from .. import CredentialUnavailableError
from .._constants import DEVELOPER_SIGN_ON_CLIENT_ID
from .._internal import AuthCodeRedirectServer, InteractiveCredential, wrap_exceptions

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    # pylint:disable=unused-import
    from typing import Any


class InteractiveBrowserCredential(InteractiveCredential):
    """Opens a browser to interactively authenticate a user.

    :func:`~get_token` opens a browser to a login URL provided by Azure Active Directory and authenticates a user
    there with the authorization code flow, using PKCE (Proof Key for Code Exchange) internally to protect the code.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: an Azure Active Directory tenant ID. Defaults to the "organizations" tenant, which can
        authenticate work or school accounts.
    :keyword str client_id: Client ID of the Azure Active Directory application users will sign in to. If
        unspecified, users will authenticate to an Azure development application.
    :keyword str login_hint: a username suggestion to pre-fill the login page's username/email address field. A user
        may still log in with a different username.
    :keyword str redirect_uri: a redirect URI for the application identified by `client_id` as configured in Azure
        Active Directory, for example "http://localhost:8400". This is only required when passing a value for
        **client_id**, and must match a redirect URI in the application's registration. The credential must be able to
        bind a socket to this URI.
    :keyword AuthenticationRecord authentication_record: :class:`AuthenticationRecord` returned by :func:`authenticate`
    :keyword bool disable_automatic_authentication: if True, :func:`get_token` will raise
        :class:`AuthenticationRequiredError` when user interaction is required to acquire a token. Defaults to False.
    :keyword cache_persistence_options: configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword int timeout: seconds to wait for the user to complete authentication. Defaults to 300 (5 minutes).
    :keyword bool allow_multitenant_authentication: when True, enables the credential to acquire tokens from any tenant
        the user is registered in. When False, which is the default, the credential will acquire tokens only from the
        user's home tenant or the tenant specified by **tenant_id**.
    :raises ValueError: invalid **redirect_uri**
    """

    def __init__(self, **kwargs):
        # type: (**Any) -> None
        redirect_uri = kwargs.pop("redirect_uri", None)
        if redirect_uri:
            self._parsed_url = urlparse(redirect_uri)
            if not (self._parsed_url.hostname and self._parsed_url.port):
                raise ValueError('"redirect_uri" must be a URL with port number, for example "http://localhost:8400"')
        else:
            self._parsed_url = None

        self._login_hint = kwargs.pop("login_hint", None)
        self._timeout = kwargs.pop("timeout", 300)
        self._server_class = kwargs.pop("_server_class", AuthCodeRedirectServer)
        client_id = kwargs.pop("client_id", DEVELOPER_SIGN_ON_CLIENT_ID)
        super(InteractiveBrowserCredential, self).__init__(client_id=client_id, **kwargs)

    @wrap_exceptions
    def _request_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> dict

        # start an HTTP server to receive the redirect
        server = None
        if self._parsed_url:
            try:
                redirect_uri = "http://{}:{}".format(self._parsed_url.hostname, self._parsed_url.port)
                server = self._server_class(self._parsed_url.hostname, self._parsed_url.port, timeout=self._timeout)
            except socket.error:
                raise CredentialUnavailableError(message="Couldn't start an HTTP server on " + redirect_uri)
        else:
            for port in range(8400, 9000):
                try:
                    server = self._server_class("localhost", port, timeout=self._timeout)
                    redirect_uri = "http://localhost:{}".format(port)
                    break
                except socket.error:
                    continue  # keep looking for an open port

        if not server:
            raise CredentialUnavailableError(message="Couldn't start an HTTP server on localhost")

        # get the url the user must visit to authenticate
        scopes = list(scopes)  # type: ignore
        claims = kwargs.get("claims")
        app = self._get_app(**kwargs)
        flow = app.initiate_auth_code_flow(
            scopes,
            redirect_uri=redirect_uri,
            prompt="select_account",
            claims_challenge=claims,
            login_hint=self._login_hint,
        )
        if "auth_uri" not in flow:
            raise CredentialUnavailableError("Failed to begin authentication flow")

        if not _open_browser(flow["auth_uri"]):
            raise CredentialUnavailableError(message="Failed to open a browser")

        # block until the server times out or receives the post-authentication redirect
        response = server.wait_for_redirect()
        if not response:
            raise ClientAuthenticationError(
                message="Timed out after waiting {} seconds for the user to authenticate".format(self._timeout)
            )

        # redeem the authorization code for a token
        return app.acquire_token_by_auth_code_flow(flow, response, scopes=scopes, claims_challenge=claims)


def _open_browser(url):
    opened = webbrowser.open(url)
    if not opened:
        uname = platform.uname()
        system = uname[0].lower()
        release = uname[2].lower()
        if "microsoft" in release and system == "linux":
            kwargs = {}
            if platform.python_version() >= "3.3":
                kwargs["timeout"] = 5

            try:
                exit_code = subprocess.call(
                    ["powershell.exe", "-NoProfile", "-Command", 'Start-Process "{}"'.format(url)], **kwargs
                )
                opened = exit_code == 0
            except Exception:  # pylint:disable=broad-except
                # powershell.exe isn't available, or the subprocess timed out
                pass
    return opened
