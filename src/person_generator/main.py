from __future__ import annotations

import sys

sys.path.append(".")

from pathlib import Path

from person_generator.constants import CSV_DTYPES_MAP
from person_generator.utils.df_utils import (
    append_people_to_csv,
    append_people_to_parquet,
    convert_pq_to_csv,
)

from core.constants import DATA_DIR, OUTPUT_CSV_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR, RAW_DIR
from core.dependencies import DEFAULT_FAKER, new_faker
from domain.person import (
    Person,
    generate_people,
    generate_random_person,
)
from faker import Faker
from loguru import logger as log
import polars as pl
from red_utils.ext.context_managers import SimpleSpinner
from red_utils.ext.loguru_utils import LoguruSinkStdOut, init_logger

for d in [DATA_DIR, OUTPUT_CSV_DIR, OUTPUT_PQ_DIR, OUTPUT_DIR, RAW_DIR]:
    if not d.exists():
        try:
            d.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            log.error(f"Unhandled exception creating path: {d}. Details: {exc}")


def generate_main(
    fake: Faker = None,
    num_people: int = 3,
    csv_output_path: Path = Path(f"{RAW_DIR}/people.csv"),
    pq_output_path: Path = Path(f"{RAW_DIR}/people.parquet"),
    save_csv: bool = True,
) -> list[Person]:
    if fake is None:
        fake = Faker()

    use_spinner: bool = False

    with SimpleSpinner(f"Generating {num_people} Person object(s)..."):
        people = generate_people(fake=fake, num=num_people)

    if len(people) > 20000:
        use_spinner = True

    if use_spinner:
        with SimpleSpinner(
            f"Saving [{len(people)}] Person objects to CSV file '{csv_output_path}' ... "
        ):
            # append_people_to_csv(people=people, output_file=csv_output_path)
            append_people_to_parquet(people=people, output_file=pq_output_path)
    else:
        # append_people_to_csv(people=people, output_file=csv_output_path)
        append_people_to_parquet(people=people, output_file=pq_output_path)

    if save_csv:
        log.info(f"Converting Parquet file to CSV")
        convert_pq_to_csv(output_csv=Path(f"{RAW_DIR}/people.csv"))


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])
    log.info("Start Fake person generator.")

    if not RAW_DIR.exists():
        log.warning(f"Dir {RAW_DIR} does not exist, creating")
        RAW_DIR.mkdir(parents=True, exist_ok=True)

    ## Uses the global faker initialized at app start
    default_fake = DEFAULT_FAKER
    ## New data each time
    fake = new_faker()
    ## Same data each time
    fake_static = new_faker(seed=142356893021)

    people = generate_main(fake, num_people=500)
