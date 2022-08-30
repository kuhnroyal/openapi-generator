# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class EnumArrays(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            
            
            class just_symbol(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        ">=": "GREATER_THAN_EQUALS",
                        "$": "DOLLAR",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def GREATER_THAN_EQUALS(cls):
                    return cls(">=")
                
                @classmethod
                @property
                def DOLLAR(cls):
                    return cls("$")
            
            
            class array_enum(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.SchemaEnumMakerClsFactory(
                            enum_value_to_name={
                                "fish": "FISH",
                                "crab": "CRAB",
                            }
                        ),
                        schemas.StrSchema
                    ):
                        
                        @classmethod
                        @property
                        def FISH(cls):
                            return cls("fish")
                        
                        @classmethod
                        @property
                        def CRAB(cls):
                            return cls("crab")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array_enum':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "just_symbol": just_symbol,
                "array_enum": array_enum,
            }
        additional_properties = schemas.AnyTypeSchema
    
    just_symbol: MetaOapg.properties.just_symbol
    array_enum: MetaOapg.properties.array_enum
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["just_symbol"]) -> MetaOapg.properties.just_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["array_enum"]) -> MetaOapg.properties.array_enum: ...
    
    def __getitem__(self, name: str) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        just_symbol: typing.Union[MetaOapg.properties.just_symbol, str, schemas.Unset] = schemas.unset,
        array_enum: typing.Union[MetaOapg.properties.array_enum, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'EnumArrays':
        return super().__new__(
            cls,
            *args,
            just_symbol=just_symbol,
            array_enum=array_enum,
            _configuration=_configuration,
            **kwargs,
        )
