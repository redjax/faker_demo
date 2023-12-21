from typing import Union
from pydantic import BaseModel, Field, field_validator, ValidationError
from loguru import logger as log

import pendulum


class Person(BaseModel):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    dob: pendulum.Date = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    job: str = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

    @property
    def age(self) -> int:
        today = pendulum.now()
        _age = (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )

        return _age
