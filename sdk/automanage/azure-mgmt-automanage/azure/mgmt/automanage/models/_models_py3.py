# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._automanage_client_enums import *


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Account(TrackedResource):
    """Definition of the Automanage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param identity: The identity of the Automanage account.
    :type identity: ~automanage_client.models.AccountIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'AccountIdentity'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["AccountIdentity"] = None,
        **kwargs
    ):
        super(Account, self).__init__(tags=tags, location=location, **kwargs)
        self.identity = identity


class AccountIdentity(msrest.serialization.Model):
    """Identity for the Automanage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal id of Automanage account identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the Automanage account.
    :vartype tenant_id: str
    :param type: The type of identity used for the Automanage account. Currently, the only
     supported type is 'SystemAssigned', which implicitly creates an identity. Possible values
     include: "SystemAssigned", "None".
    :type type: str or ~automanage_client.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "ResourceIdentityType"]] = None,
        **kwargs
    ):
        super(AccountIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class AccountList(msrest.serialization.Model):
    """The response of the list Account operation.

    :param value: Result of the list Account operation.
    :type value: list[~automanage_client.models.Account]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Account]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Account"]] = None,
        **kwargs
    ):
        super(AccountList, self).__init__(**kwargs)
        self.value = value


class UpdateResource(msrest.serialization.Model):
    """Represents an update resource.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(UpdateResource, self).__init__(**kwargs)
        self.tags = tags


class AccountUpdate(UpdateResource):
    """Definition of the Automanage account.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param identity: The identity of the Automanage account.
    :type identity: ~automanage_client.models.AccountIdentity
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'AccountIdentity'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["AccountIdentity"] = None,
        **kwargs
    ):
        super(AccountUpdate, self).__init__(tags=tags, **kwargs)
        self.identity = identity


class ConfigurationProfileAssignment(Resource):
    """Configuration profile assignment is an association between a VM and automanage profile configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param properties: Properties of the configuration profile assignment.
    :type properties: ~automanage_client.models.ConfigurationProfileAssignmentProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfigurationProfileAssignmentProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["ConfigurationProfileAssignmentProperties"] = None,
        **kwargs
    ):
        super(ConfigurationProfileAssignment, self).__init__(**kwargs)
        self.properties = properties


class ConfigurationProfileAssignmentCompliance(msrest.serialization.Model):
    """The compliance status for the configuration profile assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar update_status: The state of compliance, which only appears in the response. Possible
     values include: "Succeeded", "Failed", "Created".
    :vartype update_status: str or ~automanage_client.models.UpdateStatus
    """

    _validation = {
        'update_status': {'readonly': True},
    }

    _attribute_map = {
        'update_status': {'key': 'updateStatus', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentCompliance, self).__init__(**kwargs)
        self.update_status = None


class ConfigurationProfileAssignmentList(msrest.serialization.Model):
    """The response of the list configuration profile assignment operation.

    :param value: Result of the list configuration profile assignment operation.
    :type value: list[~automanage_client.models.ConfigurationProfileAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationProfileAssignment]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ConfigurationProfileAssignment"]] = None,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentList, self).__init__(**kwargs)
        self.value = value


class ConfigurationProfileAssignmentProperties(msrest.serialization.Model):
    """Automanage configuration profile assignment properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param configuration_profile: A value indicating configuration profile. Possible values
     include: "Azure virtual machine best practices – Dev/Test", "Azure virtual machine best
     practices – Production".
    :type configuration_profile: str or ~automanage_client.models.ConfigurationProfile
    :param target_id: The target VM resource URI.
    :type target_id: str
    :param account_id: The Automanage account ARM Resource URI.
    :type account_id: str
    :param configuration_profile_preference_id: The configuration profile custom preferences ARM
     resource URI.
    :type configuration_profile_preference_id: str
    :ivar provisioning_status: The state of onboarding, which only appears in the response.
     Possible values include: "Succeeded", "Failed", "Created".
    :vartype provisioning_status: str or ~automanage_client.models.ProvisioningStatus
    :param compliance: The configuration setting for the configuration profile.
    :type compliance: ~automanage_client.models.ConfigurationProfileAssignmentCompliance
    """

    _validation = {
        'provisioning_status': {'readonly': True},
    }

    _attribute_map = {
        'configuration_profile': {'key': 'configurationProfile', 'type': 'str'},
        'target_id': {'key': 'targetId', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'configuration_profile_preference_id': {'key': 'configurationProfilePreferenceId', 'type': 'str'},
        'provisioning_status': {'key': 'provisioningStatus', 'type': 'str'},
        'compliance': {'key': 'compliance', 'type': 'ConfigurationProfileAssignmentCompliance'},
    }

    def __init__(
        self,
        *,
        configuration_profile: Optional[Union[str, "ConfigurationProfile"]] = None,
        target_id: Optional[str] = None,
        account_id: Optional[str] = None,
        configuration_profile_preference_id: Optional[str] = None,
        compliance: Optional["ConfigurationProfileAssignmentCompliance"] = None,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentProperties, self).__init__(**kwargs)
        self.configuration_profile = configuration_profile
        self.target_id = target_id
        self.account_id = account_id
        self.configuration_profile_preference_id = configuration_profile_preference_id
        self.provisioning_status = None
        self.compliance = compliance


class ConfigurationProfilePreference(TrackedResource):
    """Definition of the configuration profile preference.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param properties: Properties of the configuration profile preference.
    :type properties: ~automanage_client.models.ConfigurationProfilePreferenceProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfigurationProfilePreferenceProperties'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["ConfigurationProfilePreferenceProperties"] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreference, self).__init__(tags=tags, location=location, **kwargs)
        self.properties = properties


class ConfigurationProfilePreferenceAntiMalware(msrest.serialization.Model):
    """Automanage configuration profile Antimalware preferences.

    :param enable_real_time_protection: Enables or disables Real Time Protection. Possible values
     include: "True", "False".
    :type enable_real_time_protection: str or ~automanage_client.models.EnableRealTimeProtection
    :param exclusions: Extensions, Paths and Processes that must be excluded from scan.
    :type exclusions: object
    :param run_scheduled_scan: Enables or disables a periodic scan for antimalware. Possible values
     include: "True", "False".
    :type run_scheduled_scan: str or ~automanage_client.models.RunScheduledScan
    :param scan_type: Type of scheduled scan. Possible values include: "Quick", "Full".
    :type scan_type: str or ~automanage_client.models.ScanType
    :param scan_day: Schedule scan settings day.
    :type scan_day: str
    :param scan_time_in_minutes: Schedule scan settings time.
    :type scan_time_in_minutes: str
    """

    _attribute_map = {
        'enable_real_time_protection': {'key': 'enableRealTimeProtection', 'type': 'str'},
        'exclusions': {'key': 'exclusions', 'type': 'object'},
        'run_scheduled_scan': {'key': 'runScheduledScan', 'type': 'str'},
        'scan_type': {'key': 'scanType', 'type': 'str'},
        'scan_day': {'key': 'scanDay', 'type': 'str'},
        'scan_time_in_minutes': {'key': 'scanTimeInMinutes', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        enable_real_time_protection: Optional[Union[str, "EnableRealTimeProtection"]] = None,
        exclusions: Optional[object] = None,
        run_scheduled_scan: Optional[Union[str, "RunScheduledScan"]] = None,
        scan_type: Optional[Union[str, "ScanType"]] = None,
        scan_day: Optional[str] = None,
        scan_time_in_minutes: Optional[str] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceAntiMalware, self).__init__(**kwargs)
        self.enable_real_time_protection = enable_real_time_protection
        self.exclusions = exclusions
        self.run_scheduled_scan = run_scheduled_scan
        self.scan_type = scan_type
        self.scan_day = scan_day
        self.scan_time_in_minutes = scan_time_in_minutes


class ConfigurationProfilePreferenceList(msrest.serialization.Model):
    """The response of the list ConfigurationProfilePreference operation.

    :param value: Result of the list ConfigurationProfilePreference operation.
    :type value: list[~automanage_client.models.ConfigurationProfilePreference]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationProfilePreference]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ConfigurationProfilePreference"]] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceList, self).__init__(**kwargs)
        self.value = value


class ConfigurationProfilePreferenceProperties(msrest.serialization.Model):
    """Automanage configuration profile preference properties.

    :param vm_backup: The custom preferences for Azure VM Backup.
    :type vm_backup: ~automanage_client.models.ConfigurationProfilePreferenceVmBackup
    :param anti_malware: The custom preferences for Azure Antimalware.
    :type anti_malware: ~automanage_client.models.ConfigurationProfilePreferenceAntiMalware
    """

    _attribute_map = {
        'vm_backup': {'key': 'vmBackup', 'type': 'ConfigurationProfilePreferenceVmBackup'},
        'anti_malware': {'key': 'antiMalware', 'type': 'ConfigurationProfilePreferenceAntiMalware'},
    }

    def __init__(
        self,
        *,
        vm_backup: Optional["ConfigurationProfilePreferenceVmBackup"] = None,
        anti_malware: Optional["ConfigurationProfilePreferenceAntiMalware"] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceProperties, self).__init__(**kwargs)
        self.vm_backup = vm_backup
        self.anti_malware = anti_malware


class ConfigurationProfilePreferenceUpdate(UpdateResource):
    """Definition of the configuration profile preference.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param properties: Properties of the configuration profile preference.
    :type properties: ~automanage_client.models.ConfigurationProfilePreferenceProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'ConfigurationProfilePreferenceProperties'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["ConfigurationProfilePreferenceProperties"] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceUpdate, self).__init__(tags=tags, **kwargs)
        self.properties = properties


class ConfigurationProfilePreferenceVmBackup(msrest.serialization.Model):
    """Automanage configuration profile VM Backup preferences.

    :param time_zone: TimeZone optional input as string. For example: Pacific Standard Time.
    :type time_zone: str
    :param instant_rp_retention_range_in_days: Instant RP retention policy range in days.
    :type instant_rp_retention_range_in_days: int
    :param retention_policy: Retention policy with the details on backup copy retention ranges.
    :type retention_policy: str
    :param schedule_policy: Backup schedule specified as part of backup policy.
    :type schedule_policy: str
    """

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'instant_rp_retention_range_in_days': {'key': 'instantRpRetentionRangeInDays', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'str'},
        'schedule_policy': {'key': 'schedulePolicy', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        time_zone: Optional[str] = None,
        instant_rp_retention_range_in_days: Optional[int] = None,
        retention_policy: Optional[str] = None,
        schedule_policy: Optional[str] = None,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceVmBackup, self).__init__(**kwargs)
        self.time_zone = time_zone
        self.instant_rp_retention_range_in_days = instant_rp_retention_range_in_days
        self.retention_policy = retention_policy
        self.schedule_policy = schedule_policy


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(msrest.serialization.Model):
    """The resource management error response.

    :param error: The error object.
    :type error: ~automanage_client.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseError"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseError(msrest.serialization.Model):
    """The error object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~automanage_client.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~automanage_client.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class Operation(msrest.serialization.Model):
    """Automanage REST API operation.

    :param name: Operation name: For ex.
     providers/Microsoft.Automanage/configurationProfileAssignments/write or read.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: str
    :param display: Provider, Resource, Operation and description values.
    :type display: ~automanage_client.models.OperationDisplay
    :param status_code: Service provider: Microsoft.Automanage.
    :type status_code: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'status_code': {'key': 'properties.statusCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_data_action: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        status_code: Optional[str] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display
        self.status_code = status_code


class OperationDisplay(msrest.serialization.Model):
    """Provider, Resource, Operation and description values.

    :param provider: Service provider: Microsoft.Automanage.
    :type provider: str
    :param resource: Resource on which the operation is performed:  For ex.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description about operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(msrest.serialization.Model):
    """The response model for the list of Automanage operations.

    :param value: List of Automanage operations supported by the Automanage resource provider.
    :type value: list[~automanage_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = value


class ProxyResource(Resource):
    """The resource model definition for a ARM proxy resource. It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)