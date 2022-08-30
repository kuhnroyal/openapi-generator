# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class RefInProperty(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
        
            @classmethod
            @property
            def a(cls) -> typing.Type['PropertyNamedRefThatIsNotAReference']:
                return PropertyNamedRefThatIsNotAReference
            __annotations__ = {
                "a": a,
            }
        additional_properties = schemas.AnyTypeSchema

    
    a: 'PropertyNamedRefThatIsNotAReference'
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["a"]) -> 'PropertyNamedRefThatIsNotAReference': ...
    
    def __getitem__(self, name: str) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        a: typing.Union['PropertyNamedRefThatIsNotAReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'RefInProperty':
        return super().__new__(
            cls,
            *args,
            a=a,
            _configuration=_configuration,
            **kwargs,
        )

from unit_test_api.model.property_named_ref_that_is_not_a_reference import PropertyNamedRefThatIsNotAReference
