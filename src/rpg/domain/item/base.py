from __future__ import annotations

from pydantic import BaseModel, Field, ValidationError, field_validator


class ItemBase(BaseModel):
    name: str = Field(default=None)
    description: str = Field(default=None)
