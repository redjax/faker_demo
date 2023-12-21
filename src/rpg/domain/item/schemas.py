from __future__ import annotations

from .base import ItemBase

from pydantic import BaseModel, Field, ValidationError, field_validator


class Item(ItemBase):
    pass


class Potion(Item):
    healing: int = Field(default=None)


class Coin(Item):
    value: int = Field(default=0)
