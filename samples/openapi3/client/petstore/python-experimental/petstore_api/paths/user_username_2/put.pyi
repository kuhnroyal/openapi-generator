# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from petstore_api.model.user import User

# path params
UsernameSchema = schemas.StrSchema
# body param
SchemaForRequestBodyApplicationJson = User
