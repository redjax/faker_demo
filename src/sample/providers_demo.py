from faker import Faker
import polars as pl
from dateutil.relativedelta import relativedelta

fake = Faker()

seed: int | None = None

if seed:
    Faker.seed(seed)


def generate_persons(num=1):
    fake = Faker()
    rows = [
        {
            "person_id": fake.uuid4(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address(),
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=75),
            "ssn": fake.ssn(),
        }
        for x in range(num)
    ]

    return pl.DataFrame(rows)


if __name__ == "__main__":
    persons = generate_persons(1000)
    print(persons)
