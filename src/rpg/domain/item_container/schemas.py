from __future__ import annotations

from .base import InventoryBase

from pydantic import BaseModel, Field, ValidationError, field_validator


class Inventory(InventoryBase):
    pass
