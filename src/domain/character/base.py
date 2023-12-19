from pydantic import BaseModel, Field, field_validator, ValidationError

from domain.item_container import Inventory, new_inventory


class CharacterBase(BaseModel):
    name: str = Field(default=None)
    character_class: str = Field(default=None)
    health: int = Field(default=100)
    inventory: Inventory = Field(default_factory=new_inventory)
