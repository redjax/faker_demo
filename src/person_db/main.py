import sys

sys.path.append(".")

from pathlib import Path

from faker import Faker
from loguru import logger as log
import polars as pl

from red_utils.ext.loguru_utils import init_logger, LoguruSinkStdOut

from core.dependencies import new_faker, DEFAULT_FAKER
from person_db.domain.person import Person
from person_db.constants import DATA_DIR, RAW_DIR, DF_DTYPES_MAP


def generate_random_person(fake: Faker = None) -> Person:
    """Generate fake data with Faker and populate a Person object."""
    person = Person()

    person.first_name = fake.first_name()
    person.last_name = fake.last_name()
    person.dob = fake.date_of_birth(minimum_age=13, maximum_age=75)
    person.email = f"{fake.user_name()}@{fake.free_email_domain()}"

    return person


def generate_people(num: int = 3) -> list[Person]:
    """Generate multiple Person instances at once."""
    people: list[Person] = []

    count: int = 0
    while count < num:
        person: Person = generate_random_person(fake=fake)
        log.debug(f"Person: {person}, Age: {person.age}")

        people.append(person)

        count += 1

    return people


def append_people(
    people: list[Person] = None, output_file: Path = Path(f"{RAW_DIR}/people.csv")
) -> bool:
    people_dfs: list[pl.DataFrame] = []

    for p in people:
        p_df = pl.DataFrame(p.model_dump())
        log.debug(f"Person DataFrame:\n{p_df}")
        people_dfs.append(p_df)

    df = pl.concat(people_dfs)
    log.debug(df.head(5))

    if output_file.exists():
        log.warning(
            f"Output already exists: {output_file}. Loading to a DataFrame to concat new data"
        )
        existing_data: pl.DataFrame = pl.read_csv(output_file, dtypes=DF_DTYPES_MAP)
        log.debug(f"Existing:\n{existing_data.head(5)}")
    else:
        existing_data = None

    if existing_data is not None:
        df = pl.concat([df, existing_data])
    try:
        df.write_csv(file=output_file)

        return True
    except Exception as exc:
        log.error(exc)

        return False


def main(fake: Faker = None, num_people: int = 3):
    if fake is None:
        fake = Faker()

    people = generate_people(num=num_people)
    log.info(f"Generated [{len(people)}] people.")

    append_people(people=people)


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])
    log.info("Start Fake person database.")

    if not RAW_DIR.exists():
        log.warning(f"Dir {RAW_DIR} does not exist, creating")
        RAW_DIR.mkdir(parents=True, exist_ok=True)

    ## Uses the global faker initialized at app start
    default_fake = DEFAULT_FAKER
    ## New data each time
    fake = new_faker()
    ## Same data each time
    fake_static = new_faker(seed=142356893021)

    main(fake)
