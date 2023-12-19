from pydantic import BaseModel, Field, field_validator, ValidationError


class ItemBase(BaseModel):
    name: str = Field(default=None)
    description: str = Field(default=None)
