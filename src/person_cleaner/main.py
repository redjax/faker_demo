from __future__ import annotations

import sys

sys.path.append(".")

import random
from pathlib import Path

from core.constants import DATA_DIR, OUTPUT_CSV_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR, RAW_DIR
from domain.person import Person, generate_random_person
from loguru import logger as log
from person_generator.constants import (
    CSV_DTYPES_MAP,
    DF_DTYPES_MAP,
    RAW_CSV_PEOPLE_FILE,
    RAW_PQ_PEOPLE_FILE,
)
from person_cleaner.constants import CLEANED_PQ_FILE, CLEANED_CSV_FILE
import polars as pl
from red_utils.ext.context_managers import SimpleSpinner
from red_utils.ext.loguru_utils import LoguruSinkStdOut, init_logger


def df_dedupe(df: pl.DataFrame = None, subset: list[str] = []) -> pl.DataFrame:
    """Drop duplicate records in a DataFrame."""
    if df is None or df.is_empty():
        raise ValueError("Missing a DataFrame to deduplicate.")
    if subset is None or not subset:
        log.warning(
            f"Subset is empty, but must contain at least one row. Setting subset to ['id']"
        )
        subset = ["id"]

    log.info(f"Deduplicating DataFrame. Original shape: {df.shape}")

    try:
        _dedupe = df.unique(subset=subset)

        log.info(f"DataFrame duplicates removed. Deduplicated shape: {_dedupe.shape}")

        return _dedupe
    except Exception as exc:
        msg = Exception(f"Unhandled exception deduplicating DataFrame. Details: {exc}")
        log.error(msg)

        raise msg


def get_rand_list_index(lst: list = None) -> int:
    """Return a random index by using random.randint(0, len(lst) - 1)."""
    if lst is None or len(lst) == 0:
        raise ValueError("Input list empty or None.")

    lst_len: int = len(lst)
    rand_index: int = random.randint(0, lst_len - 1)

    return rand_index


def load_existing_people_from_files() -> pl.DataFrame:
    """Load existing Person records from files."""
    csv_df: pl.DataFrame = pl.read_csv(RAW_CSV_PEOPLE_FILE, dtypes=CSV_DTYPES_MAP)
    log.debug(f"CSV data:\n{csv_df.head(5)}")

    pq_df: pl.DataFrame = pl.read_parquet(RAW_PQ_PEOPLE_FILE, use_pyarrow=True)
    log.debug(f"Parquet data:\n{pq_df.head(5)}")

    return (csv_df, pq_df)


def convert_dicts_to_people(dicts: list[dict] = []) -> list[Person]:
    """Convert a list of dict objects converted from a DataFrame to a list of Person objects."""
    people: list[Person] = []

    for p in dicts:
        try:
            person: Person = Person.model_validate(p)
            people.append(person)
        except Exception as exc:
            log.error(
                f"Unhandled exception converting row to Person object. Dict ({type(p)}): {p}. Details: {exc}"
            )
            pass

    return people


def run_cleaning_operations(save_csv: bool = False):
    with SimpleSpinner("Loading existing data from files into DataFrames... "):
        preload_dfs: tuple[pl.DataFrame] = load_existing_people_from_files()

    csv_df: pl.DataFrame = preload_dfs[0]
    pq_df: pl.DataFrame = preload_dfs[1]

    csv_df = df_dedupe(df=csv_df)
    pq_df = df_dedupe(df=pq_df)

    with SimpleSpinner(f"Converting [{pq_df.shape[0]}] row(s) to dict(s)... "):
        person_dicts: list[dict] = pq_df.to_dicts()

    log.info(f"Converted [{len(person_dicts)}] Person row(s) to Python dict(s)")
    person_dict_sample_index = get_rand_list_index(lst=person_dicts)
    log.debug(
        f"Sample Person dict (index: [{person_dict_sample_index}]): {person_dicts[person_dict_sample_index]}"
    )

    with SimpleSpinner(
        f"Converting [{len(person_dicts)}] person_dict(s) to Person object(s)... "
    ):
        people: list[Person] = convert_dicts_to_people(person_dicts)

    log.info(f"Converted [{len(people)}] dict(s) to Person object(s)")
    person_sample_index = get_rand_list_index(lst=people)
    log.debug(
        f"Sample Person (index: [{person_sample_index}]): {people[person_sample_index]}"
    )

    cleaned_df: pl.DataFrame = pq_df
    cleaned_df = cleaned_df.with_columns(
        pl.col("age").cast(pl.Int32),
        pl.col("dob").cast(pl.Date),
        pl.col("addr_zip").cast(pl.Int32),
        pl.col("addr_housenum").cast(pl.Int32),
    )
    log.debug(f"Cleaned DF preview:\n{cleaned_df.head(5)}")
    log.debug(f"Cleaned DF dtypes:\n{cleaned_df.dtypes}")

    log.info(f"Outputting cleaned_df to {CLEANED_PQ_FILE}")

    try:
        cleaned_df.write_parquet(file=CLEANED_PQ_FILE, use_pyarrow=True)
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception saving cleaned DataFrame to path: '{CLEANED_PQ_FILE}'. Details: {exc}"
        )
        log.error(msg)

        raise msg

    if save_csv:
        log.info(f"save_csv=True, saving cleaned DataFrame to {CLEANED_CSV_FILE}")
        try:
            cleaned_df.write_csv(file=CLEANED_CSV_FILE)
        except Exception as exc:
            msg = Exception(
                f"Unhandled exception saving cleaned DataFrame to path: '{CLEANED_CSV_FILE}'. Details: {exc}"
            )
            log.error(msg)

            raise msg


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])

    log.info(f"Person cleaner start")

    run_cleaning_operations()
