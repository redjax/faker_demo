from pydantic import BaseModel, Field, field_validator, ValidationError

from rpg.domain.item import Item


class InventoryBase(BaseModel):
    items: list[Item] = Field(default=[])

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            print(f"- {item.name}: {item.description}")
