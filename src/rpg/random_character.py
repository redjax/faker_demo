from __future__ import annotations

import sys

sys.path.append(".")

from faker import Faker
import random

from domain.item import Item, Potion, Coin
from domain.item_container import Inventory, new_inventory
from domain.character import Character


fake: Faker = Faker()


def generate_random_character() -> Character:
    name = fake.word()
    character_class = random.choice(["Warrior", "Mage", "Rogue"])
    description = fake.sentence()
    health: int = random.randint(30, 100)

    return Character(
        name=name,
        character_class=character_class,
        description=description,
        health=health,
    )


def generate_random_potion() -> Potion:
    name = fake.word()
    description = fake.sentence()
    healing = random.randint(10, 30)

    return Potion(name=name, description=description, healing=healing)


def generate_random_coin() -> Coin:
    name = fake.word()
    description = fake.sentence()
    value = random.randint(1, 10)

    return Coin(name=name, description=description, value=value)


def main():
    hero = generate_random_character()
    villain = generate_random_character()

    health_potion = generate_random_potion()
    mana_potion = generate_random_potion()
    gold_coin = generate_random_coin()

    hero.inventory.add_item(health_potion)
    hero.inventory.add_item(gold_coin)

    villain.inventory.add_item(mana_potion)
    villain.inventory.add_item(gold_coin)

    print(
        f"""Hero:
    {hero}
    
Villain:

    {villain}
"""
    )


if __name__ == "__main__":
    main()
