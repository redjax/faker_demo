from __future__ import annotations

import datetime
from typing import Union
from uuid import UUID, uuid4

from loguru import logger as log
import pendulum
from pydantic import BaseModel, Field, ValidationError, field_validator


class Person(BaseModel):
    id: str = Field(default_factory=uuid4)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    dob: datetime.date = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    job: str = Field(default=None)
    company: str = Field(default=None)
    license: str = Field(default=None)
    vin: str = Field(default=None)
    addr_housenum: Union[int, str] = Field(default=None)
    addr_street: str = Field(default=None)
    addr_city: str = Field(default=None)
    addr_state: str = Field(default=None)
    addr_zip: str = Field(default=None)
    addr_country: str = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

    @field_validator("addr_housenum")
    def validate_addr_housenum(cls, v) -> str:
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValidationError

    @property
    def age(self) -> int:
        today = pendulum.now()
        _age = (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )

        return _age
