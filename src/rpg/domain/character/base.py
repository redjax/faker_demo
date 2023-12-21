from __future__ import annotations

from rpg.domain.item_container import Inventory, new_inventory

from pydantic import BaseModel, Field, ValidationError, field_validator


class CharacterBase(BaseModel):
    name: str = Field(default=None)
    character_class: str = Field(default=None)
    health: int = Field(default=100)
    inventory: Inventory = Field(default_factory=new_inventory)
