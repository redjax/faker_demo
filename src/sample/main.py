from __future__ import annotations

from faker import Faker

fake: Faker = Faker()

name = fake.name()
address = fake.address()
text = fake.text()


def print_fake_names(count: int = 10):
    for _ in range(count):
        print(f"Name: {fake.name()}")


if __name__ == "__main__":
    # print(f"Name: {name}")
    # print(f"Address: {address}")
    # print(f"Text:\n{text}")

    # print_fake_names()

    _names = [fake.unique.first_name() for i in range(500)]
    print(_names[0:15])
