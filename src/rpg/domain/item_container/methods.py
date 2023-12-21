from __future__ import annotations

from rpg.domain.item_container import Inventory


def new_inventory() -> "Inventory":
    """Return an instantiated Inventory class object."""
    return Inventory()
