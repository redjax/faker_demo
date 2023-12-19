from typing import Union
from pydantic import BaseModel, Field, field_validator, ValidationError
from loguru import logger as log

import pendulum


class Person(BaseModel):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    dob: pendulum.DateTime = Field(default=None)
    email: str = Field(default=None)
