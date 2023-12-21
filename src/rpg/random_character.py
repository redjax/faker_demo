from __future__ import annotations

import sys

sys.path.append(".")

import random

from rpg.domain.character import Character
from rpg.domain.item import Coin, Item, Potion
from rpg.domain.item_container import Inventory, new_inventory

from faker import Faker


def generate_random_character(fake: Faker = None) -> Character:
    name = fake.first_name()
    character_class = random.choice(["Warrior", "Mage", "Rogue"])
    description = fake.sentence()
    health: int = random.randint(30, 100)

    return Character(
        name=name,
        character_class=character_class,
        description=description,
        health=health,
    )


def generate_random_potion(fake: Faker = None) -> Potion:
    name = fake.word()
    description = fake.sentence()
    healing = random.randint(10, 30)

    return Potion(name=name, description=description, healing=healing)


def generate_random_coin(fake: Faker = None) -> Coin:
    name = fake.word()
    description = fake.sentence()
    value = random.randint(1, 10)

    return Coin(name=name, description=description, value=value)


def main():
    fake: Faker = Faker()

    hero = generate_random_character(fake)
    villain = generate_random_character(fake)

    health_potion = generate_random_potion(fake)
    mana_potion = generate_random_potion(fake)
    gold_coin = generate_random_coin(fake)

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
