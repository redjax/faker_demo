from pydantic import BaseModel, Field, field_validator, ValidationError

from .base import InventoryBase


class Inventory(InventoryBase):
    pass
