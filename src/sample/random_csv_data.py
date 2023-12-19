import random
from faker import Faker
from faker.providers import DynamicProvider, BaseProvider

import polars as pl


## Static provider
class AgeProvider(BaseProvider):
    def age(self):
        return self.random_int(min=1, max=99)


## Dynamic provider
professions_provider = DynamicProvider(
    provider_name="profession",
    elements=["Doctor", "Scientist", "Nurse", "Surgeon", "Clerk", "Support"],
)

## Initialize faker object
fake: Faker = Faker()
## Add static AgeProvider class
fake.add_provider(AgeProvider)
## Add dynamic professions_provider class
fake.add_provider(professions_provider)


csv_data: list = []
csv_dfs: list[pl.DataFrame] = []

## Generate rows of CSV data
for _ in range(5):
    _data = fake.csv(
        header=(
            "name",
            "address",
            "age",
            "job",
            "license_plate",
            "vin",
            "valid",
            "phone",
            "language",
            "dob",
            "symbol",
            "employer",
        ),
        data_columns=(
            "{{name}}",
            "{{address}}",
            "{{age}}",
            "{{job}}",
            "{{license_plate}}",
            "{{vin}}",
            "{{pybool}}",
            "{{country_calling_code}}{{msisdn}}",
            "{{language_name}}",
            "{{date_of_birth}}",
            "{{emoji}}",
            "{{company}}",
        ),
        num_rows=10,
        include_row_ids=False,
    )

    with open("test-fake.csv", "a+") as f:
        f.write(_data)

df = pl.read_csv("test-fake.csv", use_pyarrow=True)
print(df.head(5))
print(f"Rows: {df.shape[0]}")
