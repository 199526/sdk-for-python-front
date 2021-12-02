# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import dataclasses
import json
import datetime
from typing import Any, List, Literal, Dict, Sequence, Set, Tuple, Optional
import pytest
import isodate
from azure.core.serialization import Model, rest_field, rest_dataclass

def modify_args(init):
    def _wrapper(self, **kwargs):
        init(self, **{
            self._get_property_name(kwarg) or kwarg: value
            for kwarg, value in kwargs.items()
        })
    return _wrapper

class BasicResource(Model):
    platform_update_domain_count: int = rest_field(name="platformUpdateDomainCount")  # How many times the platform update domain has been counted
    platform_fault_domain_count: int = rest_field(name="platformFaultDomainCount")  # How many times the platform fault domain has been counted
    virtual_machines: List[Any] = rest_field(name="virtualMachines")  # List of virtual machines

    # def __init__(
    #     self,
    #     *,
    #     platform_update_domain_count: int,
    #     platform_fault_domain_count: int,
    #     virtual_machines: List[Any],
    #     **kwargs
    # ):
    #     super().__init__(
    #         platform_update_domain_count=platform_update_domain_count,
    #         platform_fault_domain_count=platform_fault_domain_count,
    #         virtual_machines=virtual_machines,
    #         **kwargs
    #     )

class Pet(Model):

    name: str = rest_field()  # my name
    species: str = rest_field()  # my species

def test_model_and_dict_equal():

    dict_response = {
        "platformUpdateDomainCount": 5,
        "platformFaultDomainCount": 3,
        "virtualMachines": []
    }
    model = BasicResource(dict_response)
    model.platform_update_domain_count
    assert model == dict_response
    assert (
        model.platform_update_domain_count ==
        model["platformUpdateDomainCount"] ==
        dict_response["platformUpdateDomainCount"] ==
        5
    )
    assert (
        model.platform_fault_domain_count ==
        model['platformFaultDomainCount'] ==
        dict_response['platformFaultDomainCount'] ==
        3
    )
    assert (
        model.virtual_machines ==
        model['virtualMachines'] ==
        dict_response['virtualMachines'] ==
        []
    )

# def test_model_initialization():
#     dict_response = {
#         "platformUpdateDomainCount": 5,
#         "platformFaultDomainCount": 3,
#         "virtualMachines": []
#     }
#     a = BasicResource(platformUpdateDomainCount=5, platformFaultDomainCount=3, virtualMachines=[])
#     b = BasicResource(zip(['platformUpdateDomainCount', 'platformFaultDomainCount', 'virtualMachines'], [5, 3, []]))
#     c = BasicResource([('platformFaultDomainCount', 3), ('platformUpdateDomainCount', 5), ('virtualMachines', [])])
#     d = BasicResource({'virtualMachines': [], 'platformFaultDomainCount': 3, 'platformUpdateDomainCount': 5})
#     e = BasicResource({'platformFaultDomainCount': 3, 'virtualMachines': []}, platformUpdateDomainCount=5)
#     f = BasicResource(dict_response)
#     g = BasicResource(**dict_response)
#     assert a == b == c == d == e == f == g
#     dicts = [a, b, c, d, e, f, g]
#     for d in dicts:
#         assert len(d) == 3
#         assert d['platformUpdateDomainCount'] == d.platform_update_domain_count == 5
#         assert d['platformFaultDomainCount'] == d.platform_fault_domain_count == 3
#         assert d['virtualMachines'] == d.virtual_machines == []

# def test_json_roundtrip():
#     dict_response = {
#         "platformUpdateDomainCount": 5,
#         "platformFaultDomainCount": 3,
#         "virtualMachines": []
#     }
#     model = BasicResource(dict_response)
#     assert json.dumps(model) == '{"platformUpdateDomainCount": 5, "platformFaultDomainCount": 3, "virtualMachines": []}'
#     assert json.loads(json.dumps(model)) == model == dict_response

# def test_has_no_property():
#     dict_response = {
#         "platformUpdateDomainCount": 5,
#         "platformFaultDomainCount": 3,
#         "virtualMachines": [],
#         "noprop": "bonjour!"
#     }
#     model = BasicResource(dict_response)
#     assert (
#         model.platform_update_domain_count ==
#         model["platformUpdateDomainCount"] ==
#         dict_response["platformUpdateDomainCount"] ==
#         5
#     )
#     assert not hasattr(model, "no_prop")
#     with pytest.raises(AttributeError) as ex:
#         model.no_prop

#     assert str(ex.value) == "'BasicResource' object has no attribute 'no_prop'"
#     assert model["noprop"] == dict_response["noprop"] == "bonjour!"

#     # let's add it to model now

#     class BasicResourceWithProperty(BasicResource):

#         @rest_field(name="noprop")
#         def no_prop(self) -> str:
#             """Added prop"""

#     model = BasicResourceWithProperty(dict_response)
#     model.no_prop
#     assert (
#         model.no_prop ==
#         model["noprop"] ==
#         dict_response["noprop"] ==
#         "bonjour!"
#     )

# def test_original_and_attr_name_same():

#     class MyModel(Model):
#         @rest_field()
#         def hello(self) -> str:
#             """Prop with the same attr and dict name"""

#     dict_response = {"hello": "nihao"}
#     model = MyModel(dict_response)
#     assert model.hello == model["hello"] == dict_response["hello"]

# class OptionalModel(Model):

#     @rest_field()
#     def optional_str(self) -> Optional[str]:
#         """optional string property"""

#     @rest_field()
#     def optional_time(self) -> Optional[datetime.time]:
#         """optional time property"""

#     @rest_field(name="optionalDict")
#     def optional_dict(self) -> Optional[Dict[str, Optional[Pet]]]:
#         """My optional dict, that maps strings to optional Pet"""

#     @rest_field()
#     def optional_model(self) -> Optional[Pet]:
#         """My optional Pet"""

#     @rest_field()
#     def optional_myself(self) -> Optional["OptionalModel"]:
#         """My optional self"""

# def test_optional_property():

#     dict_response = {
#         "optional_str": "hello!",
#         "optional_time": None,
#         "optionalDict": {
#             "Eugene": {
#                 "name": "Eugene",
#                 "species": "Dog",
#             },
#             "Lady": None,
#         },
#         "optional_model": None,
#         "optional_myself": {
#             "optional_str": None,
#             "optional_time": '11:34:56',
#             "optionalDict": None,
#             "optional_model": {
#                 "name": "Lady",
#                 "species": "Newt"
#             },
#             "optional_myself": None
#         }
#     }

#     model = OptionalModel(dict_response)
#     assert model.optional_str == model["optional_str"] == "hello!"
#     assert model.optional_time == model["optional_time"] == None
#     assert model.optional_dict == model["optionalDict"] == {
#         "Eugene": {
#             "name": "Eugene",
#             "species": "Dog",
#         },
#         "Lady": None,
#     }
#     assert model.optional_dict["Eugene"].name == model.optional_dict["Eugene"]["name"] == "Eugene"
#     assert model.optional_dict["Lady"] is None

#     assert model.optional_myself == model["optional_myself"] == {
#         "optional_str": None,
#         "optional_time": '11:34:56',
#         "optionalDict": None,
#         "optional_model": {
#             "name": "Lady",
#             "species": "Newt"
#         },
#         "optional_myself": None
#     }
#     assert model.optional_myself.optional_str is None
#     assert model.optional_myself.optional_time == datetime.time(11, 34, 56)
#     assert model.optional_myself.optional_dict is None
#     assert model.optional_myself.optional_model.name == "Lady"
#     assert model.optional_myself.optional_model.species == "Newt"
#     assert model.optional_myself.optional_myself is None

# def test_modify_dict():
#     dict_response = {
#         "platformUpdateDomainCount": 5,
#         "platformFaultDomainCount": 3,
#         "virtualMachines": []
#     }
#     model = BasicResource(**dict_response)

#     # now let's modify the model as a dict
#     model["platformUpdateDomainCount"] = 100
#     assert model.platform_update_domain_count == model["platformUpdateDomainCount"] == 100

# def test_modify_property():
#     dict_response = {
#         "platformUpdateDomainCount": 5,
#         "platformFaultDomainCount": 3,
#         "virtualMachines": []
#     }
#     model = BasicResource(**dict_response)

#     # now let's modify the model through it's properties
#     model.platform_fault_domain_count = 2000
#     model['platformFaultDomainCount']
#     assert model.platform_fault_domain_count == model["platformFaultDomainCount"] == 2000

# def test_property_is_a_type():
#     class Fish(Model):

#         @rest_field()
#         def name(self) -> str:
#             """My Fish name"""

#         @rest_field()
#         def species(self) -> Literal['Salmon', 'Halibut']:
#             """My species"""

#     class Fishery(Model):

#         @rest_field()
#         def fish(self) -> Fish:
#             """The fish in my fishery."""

#     fishery = Fishery({"fish": {"name": "Benjamin", "species": "Salmon"}})
#     assert isinstance(fishery.fish, Fish)
#     assert fishery.fish.name == fishery.fish['name'] == fishery['fish']['name'] == "Benjamin"
#     assert fishery.fish.species == fishery.fish['species'] == fishery['fish']['species'] == "Salmon"

# def test_datetime_deserialization():
#     class DatetimeModel(Model):

#         @rest_field(name="datetimeValue")
#         def datetime_value(self) -> datetime.datetime:
#             """My datetime Value"""

#     val_str = "9999-12-31T23:59:59.999Z"
#     val = isodate.parse_datetime(val_str)
#     model = DatetimeModel({"datetimeValue": val_str})
#     assert model['datetimeValue'] == val_str
#     assert model.datetime_value == val

#     class BaseModel(Model):

#         @rest_field(name="myProp")
#         def my_prop(self) -> DatetimeModel:
#             """My property, which is an instance of DatetimeModel"""

#     model = BaseModel({"myProp": {"datetimeValue": val_str}})
#     assert isinstance(model.my_prop, DatetimeModel)
#     assert model.my_prop['datetimeValue'] == model['myProp']['datetimeValue'] == val_str
#     assert model.my_prop.datetime_value == val

# def test_date_deserialization():
#     class DateModel(Model):

#         @rest_field(name="dateValue")
#         def date_value(self) -> datetime.date:
#             """My date value"""

#     val_str = "2016-02-29"
#     val = isodate.parse_date(val_str)
#     model = DateModel({"dateValue": val_str})
#     assert model['dateValue'] == val_str
#     assert model.date_value == val

#     class BaseModel(Model):

#         @rest_field(name="myProp")
#         def my_prop(self) -> DateModel:
#             """My property, which is an instance of DateModel"""

#     model = BaseModel({"myProp": {"dateValue": val_str}})
#     assert isinstance(model.my_prop, DateModel)
#     assert model.my_prop['dateValue'] == model['myProp']['dateValue'] == val_str
#     assert model.my_prop.date_value == val

# def test_time_deserialization():
#     class TimeModel(Model):

#         @rest_field(name="timeValue")
#         def time_value(self) -> datetime.time:
#             """My time value"""

#     val_str = '11:34:56'
#     val = datetime.time(11, 34, 56)
#     model = TimeModel({"timeValue": val_str})
#     assert model['timeValue'] == val_str
#     assert model.time_value == val

#     class BaseModel(Model):

#         @rest_field(name="myProp")
#         def my_prop(self) -> TimeModel:
#             """My property, which is an instance of TimeModel"""

#     model = BaseModel({"myProp": {"timeValue": val_str}})
#     assert isinstance(model.my_prop, TimeModel)
#     assert model.my_prop['timeValue'] == model['myProp']['timeValue'] == val_str
#     assert model.my_prop.time_value == val

# class RecursiveModel(Model):

#     @rest_field()
#     def name(self) -> str:
#         """My name."""

#     @rest_field()
#     def me(self) -> "RecursiveModel":
#         """Me!"""

# def test_model_recursion():

#     dict_response = {
#         "name": "Snoopy",
#         "me": {
#             "name": "Egg",
#             "me": {
#                 "name": "Chicken"
#             }
#         }
#     }

#     model = RecursiveModel(dict_response)
#     assert model['name'] == model.name == "Snoopy"
#     assert model['me'] == {
#         "name": "Egg",
#         "me": {
#             "name": "Chicken"
#         }
#     }
#     assert isinstance(model.me, RecursiveModel)
#     assert model.me['name'] == model.me.name == "Egg"
#     assert model.me['me'] == {"name": "Chicken"}
#     assert model.me.me.name == "Chicken"

# def test_dictionary_deserialization():
#     class DictionaryModel(Model):

#         @rest_field()
#         def prop(self) -> Dict[str, datetime.datetime]:
#             """Dictionary of str to datetime.datetime"""

#     val_str = "9999-12-31T23:59:59.999Z"
#     val = isodate.parse_datetime(val_str)
#     dict_response = {
#         "prop": {
#             "datetime": val_str
#         }
#     }
#     model = DictionaryModel(dict_response)
#     assert model['prop'] == {"datetime": val_str}
#     assert model.prop == {"datetime": val}

# def test_dictionary_deserialization_model():

#     class DictionaryModel(Model):

#         @rest_field()
#         def prop(self) -> Dict[str, Pet]:
#             """Dictionary of str to pet"""

#     dict_response = {
#         "prop": {
#             "Eugene": {
#                 "name": "Eugene",
#                 "species": "Dog",
#             },
#             "Lady": {
#                 "name": "Lady",
#                 "species": "Newt",
#             }
#         }
#     }

#     model = DictionaryModel(dict_response)
#     assert model['prop'] == {
#         "Eugene": {
#             "name": "Eugene",
#             "species": "Dog",
#         },
#         "Lady": {
#             "name": "Lady",
#             "species": "Newt",
#         }
#     }
#     assert model.prop == {
#         "Eugene": Pet({"name": "Eugene", "species": "Dog"}),
#         "Lady": Pet({"name": "Lady", "species": "Newt"})
#     }
#     assert model.prop["Eugene"].name == model.prop["Eugene"]["name"] == "Eugene"
#     assert model.prop["Eugene"].species == model.prop["Eugene"]["species"] == "Dog"
#     assert model.prop["Lady"].name == model.prop["Lady"]["name"] == "Lady"
#     assert model.prop["Lady"].species == model.prop["Lady"]["species"] == "Newt"

# def test_list_deserialization():
#     class ListModel(Model):

#         @rest_field()
#         def prop(self) -> List[datetime.datetime]:
#             """Last of datetime.datetime"""

#     val_str = "9999-12-31T23:59:59.999Z"
#     val = isodate.parse_datetime(val_str)
#     dict_response = {
#         "prop": [val_str, val_str]
#     }
#     model = ListModel(dict_response)
#     assert model['prop'] == [val_str, val_str]
#     assert model.prop == [val, val]

# def test_list_deserialization_model():
#     class ListModel(Model):

#         @rest_field()
#         def prop(self) -> List[Pet]:
#             """List of pets"""

#     dict_response = {
#         "prop": [
#             {"name": "Eugene", "species": "Dog"},
#             {"name": "Lady", "species": "Newt"}
#         ]
#     }
#     model = ListModel(dict_response)
#     assert model["prop"] == [
#         {"name": "Eugene", "species": "Dog"},
#         {"name": "Lady", "species": "Newt"}
#     ]
#     assert model.prop == [
#         Pet({"name": "Eugene", "species": "Dog"}),
#         Pet({"name": "Lady", "species": "Newt"})
#     ]
#     assert len(model.prop) == 2
#     assert model.prop[0].name == model.prop[0]["name"] == "Eugene"
#     assert model.prop[0].species == model.prop[0]["species"] == "Dog"
#     assert model.prop[1].name == model.prop[1]["name"] == "Lady"
#     assert model.prop[1].species == model.prop[1]["species"] == "Newt"

# def test_set_deserialization():
#     class SetModel(Model):

#         @rest_field()
#         def prop(self) -> Set[datetime.datetime]:
#             """Set of datetime.datetime"""

#     val_str = "9999-12-31T23:59:59.999Z"
#     val = isodate.parse_datetime(val_str)
#     dict_response = {
#         "prop": set([val_str, val_str])
#     }
#     model = SetModel(dict_response)
#     assert model['prop'] == set([val_str, val_str])
#     assert model.prop == set([val, val])

# def test_tuple_deserialization():
#     class TupleModel(Model):

#         @rest_field()
#         def prop(self) -> Tuple[str, datetime.datetime]:
#             """Tuple of str and datetime"""

#     val_str = "9999-12-31T23:59:59.999Z"
#     val = isodate.parse_datetime(val_str)
#     dict_response = {
#         "prop": (val_str, val_str)
#     }
#     model = TupleModel(dict_response)
#     assert model['prop'] == (val_str, val_str)
#     assert model.prop == (val_str, val)

# def test_list_of_tuple_deserialization_model():

#     class Owner(Model):
#         @rest_field()
#         def name(self) -> str:
#             """Owner name"""

#         @rest_field()
#         def pet(self) -> Pet:
#             """Pet"""

#     class ListOfTupleModel(Model):

#         @rest_field()
#         def prop(self) -> List[Tuple[Pet, Owner]]:
#             """Tuple of Pet and Owner"""

#     eugene = {"name": "Eugene", "species": "Dog"}
#     lady = {"name": "Lady", "species": "Newt"}
#     giacamo = {"name": "Giacamo", "pet": eugene}
#     elizabeth = {"name": "Elizabeth", "pet": lady}

#     dict_response = {
#         "prop": [(eugene, giacamo), (lady, elizabeth)]
#     }
#     model = ListOfTupleModel(dict_response)
#     assert (
#         model['prop'] ==
#         model.prop ==
#         [(eugene, giacamo), (lady, elizabeth)] ==
#         [(Pet(eugene), Owner(giacamo)), (Pet(lady), Owner(elizabeth))]
#     )
#     assert len(model.prop[0]) == len(model['prop'][0]) == 2
#     assert model.prop[0][0].name == model.prop[0][0]['name'] == "Eugene"
#     assert model.prop[0][0].species == model.prop[0][0]['species'] == "Dog"
#     assert model.prop[0][1].name == "Giacamo"
#     assert model.prop[0][1].pet == model.prop[0][0]
#     assert model.prop[0][1].pet.name == model.prop[0][1]["pet"]["name"] == "Eugene"
#     assert model.prop[1][0] == model.prop[1][1].pet

# class RecursiveModel(Model):
#     name: rest_field()

#     @rest_field()
#     def name(self) -> str:
#         """My name"""

#     def _callable(thing):
#         return [RecursiveModel(t) for t in thing]

#     @rest_field(name="listOfMe", type=_callable)
#     def list_of_me(self) -> Sequence["RecursiveModel"]:
#         """A list of myself"""

#     @rest_field(name="dictOfMe")
#     def dict_of_me(self) -> Dict[str, "RecursiveModel"]:
#         """A dictionary of me"""

#     @rest_field(name="dictOfListOfMe")
#     def dict_of_list_of_me(self) -> Dict[str, List["RecursiveModel"]]:
#         """A dictionary of a list of me"""

#     @rest_field(name="listOfDictOfMe")
#     def list_of_dict_of_me(self) -> List[Dict[str, "RecursiveModel"]]:
#         """A list of a dictionary of me"""

#     @rest_field(name="tupleOfMe")
#     def tuple_of_me(self) -> Tuple["RecursiveModel", "RecursiveModel"]:
#         """A tuple of me"""

# model = RecursiveModel(list_of_me="should work")

# def test_model_recursion_complex():

#     dict_response = {
#         "name": "it's me!",
#         "listOfMe": [
#             {
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             }
#         ],
#         "dictOfMe": {
#             "me": {
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             }
#         },
#         "dictOfListOfMe": {
#             "many mes": [
#                 {
#                     "name": "it's me!",
#                     "listOfMe": None,
#                     "dictOfMe": None,
#                     "dictOfListOfMe": None,
#                     "listOfDictOfMe": None,
#                     "tupleOfMe": None,
#                 }
#             ]
#         },
#         "listOfDictOfMe": [
#             {"me": {
#                     "name": "it's me!",
#                     "listOfMe": None,
#                     "dictOfMe": None,
#                     "dictOfListOfMe": None,
#                     "listOfDictOfMe": None,
#                     "tupleOfMe": None,
#                 }
#             }
#         ],
#         "tupleOfMe": (
#             {
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             },
#             {
#                 "name": "it's me 2!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             },
#         )
#     }

#     model = RecursiveModel(dict_response)
#     model.dict_of_me = {"hello": "world"}
#     assert model.name == model['name'] == "it's me!"
#     assert model['listOfMe'] == [
#         {
#             "name": "it's me!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         }
#     ]
#     assert model.list_of_me == [RecursiveModel({
#         "name": "it's me!",
#         "listOfMe": None,
#         "dictOfMe": None,
#         "dictOfListOfMe": None,
#         "listOfDictOfMe": None,
#         "tupleOfMe": None,
#     })]
#     assert model.list_of_me[0].name == "it's me!"
#     assert model.list_of_me[0].list_of_me is None
#     assert isinstance(model.list_of_me, List)
#     assert isinstance(model.list_of_me[0], RecursiveModel)

#     assert model['dictOfMe'] == {
#         "me": {
#             "name": "it's me!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         }
#     }
#     assert model.dict_of_me == {"me": RecursiveModel({
#         "name": "it's me!",
#         "listOfMe": None,
#         "dictOfMe": None,
#         "dictOfListOfMe": None,
#         "listOfDictOfMe": None,
#         "tupleOfMe": None,
#     })}

#     assert isinstance(model.dict_of_me, Dict)
#     assert isinstance(model.dict_of_me["me"], RecursiveModel)

#     assert model['dictOfListOfMe'] == {
#         "many mes": [
#             {
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             }
#         ]
#     }
#     assert model.dict_of_list_of_me == {
#         "many mes": [
#             RecursiveModel({
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             })
#         ]
#     }
#     assert isinstance(model.dict_of_list_of_me, Dict)
#     assert isinstance(model.dict_of_list_of_me["many mes"], List)
#     assert isinstance(model.dict_of_list_of_me["many mes"][0], RecursiveModel)

#     assert model['listOfDictOfMe'] == [
#         {"me": {
#                 "name": "it's me!",
#                 "listOfMe": None,
#                 "dictOfMe": None,
#                 "dictOfListOfMe": None,
#                 "listOfDictOfMe": None,
#                 "tupleOfMe": None,
#             }
#         }
#     ]
#     assert model.list_of_dict_of_me == [{
#         "me": RecursiveModel({
#             "name": "it's me!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         })
#     }]
#     assert isinstance(model.list_of_dict_of_me, List)
#     assert isinstance(model.list_of_dict_of_me[0], Dict)
#     assert isinstance(model.list_of_dict_of_me[0]["me"], RecursiveModel)

#     assert model["tupleOfMe"] == (
#         {
#             "name": "it's me!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         },
#         {
#             "name": "it's me 2!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         },
#     )
#     assert model.tuple_of_me == (
#         RecursiveModel({
#             "name": "it's me!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         }),
#         RecursiveModel({
#             "name": "it's me 2!",
#             "listOfMe": None,
#             "dictOfMe": None,
#             "dictOfListOfMe": None,
#             "listOfDictOfMe": None,
#             "tupleOfMe": None,
#         }),
#     )
#     assert isinstance(model.tuple_of_me, Tuple)
#     assert isinstance(model.tuple_of_me[0], RecursiveModel)
#     assert isinstance(model.tuple_of_me[1], RecursiveModel)

#     assert json.loads(json.dumps(model)) == model == dict_response

# def test_literals():

#     class LiteralModel(Model):

#         @rest_field()
#         def species(self) -> Literal["Mongoose", "Eagle", "Penguin"]:
#             """My species"""

#         @rest_field()
#         def age(self) -> Literal[1, 2, 3]:
#             """My age"""

#     dict_response = {
#         "species": "Mongoose",
#         "age": 3
#     }
#     model = LiteralModel(dict_response)
#     assert model.species == model["species"] == "Mongoose"
#     assert model.age == model["age"] == 3

#     dict_response = {
#         "species": "invalid",
#         "age": 5
#     }
#     model = LiteralModel(dict_response)
#     assert model["species"] == "invalid"
#     assert model["age"] == 5

#     with pytest.raises(ValueError):
#         model.species

#     with pytest.raises(ValueError):
#         model.age
