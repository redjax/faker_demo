from pydantic import BaseModel, Field, field_validator, ValidationError

from .base import ItemBase


class Item(ItemBase):
    pass


class Potion(Item):
    healing: int = Field(default=None)


class Coin(Item):
    value: int = Field(default=0)
