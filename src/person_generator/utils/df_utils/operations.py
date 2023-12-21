from __future__ import annotations

from pathlib import Path
from uuid import UUID

from person_generator.constants import (
    CSV_DTYPES_MAP,
    DF_DTYPES_MAP,
    RAW_CSV_PEOPLE_FILE,
    RAW_PQ_PEOPLE_FILE,
)

from core.constants import DATA_DIR, OUTPUT_DIR, RAW_DIR
from domain.person import Person
from loguru import logger as log
import polars as pl


def append_people_to_csv(
    people: list[Person] = None, output_file: Path = RAW_CSV_PEOPLE_FILE
) -> bool:
    """Loop over a list of Person instances, convert to DataFrame, & write to a CSV file.

    If the file exists, new records will be appended.

    Params:
    -------
    - people (list[Person]): List of Person records to be converted to CSV rows.
    - output_file (pathlib.Path): A path to a CSV file for outputting Person rows to.
    """
    people_dfs: list[pl.DataFrame] = []

    for p in people:
        try:
            p_df = pl.DataFrame(p.model_dump())
            p_df = p_df.with_columns(age=pl.lit(p.age, dtype=pl.Int64))
            # log.debug(f"Person DataFrame:\n{p_df}")
            people_dfs.append(p_df)

        except Exception as exc:
            raise Exception(
                f"Unhandled exception converting Person to DataFrame.\n\tPerson: {p}\nException details: {exc}"
            )

    try:
        df = pl.concat(people_dfs)
    except Exception as exc:
        raise Exception(f"Unhandled exception joining DataFrames. Details: {exc}")

    log.debug(f"DF cols: {df.columns}")
    log.debug(f"DF shape: {df.shape}")
    log.debug(f"DF dtypes: {df.dtypes}")
    log.debug(f"DF head(5):\n{df.head(5)}")

    if output_file.exists():
        log.warning(
            f"Output already exists: {output_file}. Loading to a DataFrame to concat new data"
        )
        try:
            existing_data: pl.DataFrame = pl.read_csv(output_file, dtypes=DF_DTYPES_MAP)
        except Exception as exc:
            raise Exception(
                f"Unhandled exception reading CSV data in path '{output_file}' to DataFrame. Details: {exc}"
            )

        log.debug(f"Loaded [{existing_data.shape[0]}] existing Person row[s].")

        log.debug(f"Existing data DF cols: {existing_data.columns}")
        log.debug(f"Existing data DF shape: {existing_data.shape}")
        log.debug(f"Existing data DF dtypes: {existing_data.dtypes}")
        log.debug(f"Existing data DF head(5):\n{existing_data.head(5)}")

    else:
        existing_data = None

    if existing_data is not None and not existing_data.is_empty():
        pre_merge_count: int = df.shape[0]
        try:
            df: pl.DataFrame = pl.concat([df, existing_data])
        except Exception as exc:
            raise Exception(
                f"Unhandled exception joining old & new CSV data into DataFrame. Details: {exc}"
            )

        log.debug(
            f"DataFrame rows before merge: {pre_merge_count}. Rows after merge: {df.shape[0]}"
        )

    log.info(f"Saving DataFrame to {output_file}")
    try:
        # csv_df = df.with_columns([pl.col("id").cast(str).alias("id_str")])

        df.write_csv(file=output_file)

        return True

    except Exception as exc:
        log.error(exc)

        return False


def append_people_to_parquet(
    people: list[Person] = None, output_file: Path = RAW_PQ_PEOPLE_FILE
) -> bool:
    """Loop over a list of Person instances, convert to DataFrame, & write to a Parquet file.

    If the file exists, new records will be appended.

    Params:
    -------
    - people (list[Person]): List of Person records to be converted to Parquet rows.
    - output_file (pathlib.Path): A path to a Parquet file for outputting Person rows to.
    """
    people_dfs: list[pl.DataFrame] = []

    for p in people:
        try:
            p_df = pl.DataFrame(p.model_dump())
            p_df = p_df.with_columns(age=pl.lit(p.age, dtype=pl.Int64))
            # log.debug(f"Person DataFrame:\n{p_df}")
            people_dfs.append(p_df)

        except Exception as exc:
            raise Exception(
                f"Unhandled exception converting Person to DataFrame.\n\tPerson: {p}\nException details: {exc}"
            )

    try:
        df = pl.concat(people_dfs)
    except Exception as exc:
        raise Exception(f"Unhandled exception joining DataFrames. Details: {exc}")

    log.debug(f"DF cols: {df.columns}")
    log.debug(f"DF shape: {df.shape}")
    log.debug(f"DF dtypes: {df.dtypes}")
    log.debug(f"DF head(5):\n{df.head(5)}")

    if output_file.exists():
        log.warning(
            f"Output already exists: {output_file}. Loading to a DataFrame to concat new data"
        )
        try:
            existing_data: pl.DataFrame = pl.read_parquet(output_file, use_pyarrow=True)
        except Exception as exc:
            raise Exception(
                f"Unhandled exception reading CSV data in path '{output_file}' to DataFrame. Details: {exc}"
            )

        log.debug(f"Loaded [{existing_data.shape[0]}] existing Person row[s].")

        log.debug(f"Existing data DF cols: {existing_data.columns}")
        log.debug(f"Existing data DF shape: {existing_data.shape}")
        log.debug(f"Existing data DF dtypes: {existing_data.dtypes}")
        log.debug(f"Existing data DF head(5):\n{existing_data.head(5)}")

    else:
        existing_data = None

    if existing_data is not None and not existing_data.is_empty():
        pre_merge_count: int = df.shape[0]
        try:
            df: pl.DataFrame = pl.concat([df, existing_data])
        except Exception as exc:
            raise Exception(
                f"Unhandled exception joining old & new Parquet data into DataFrame. Details: {exc}"
            )

        log.debug(
            f"DataFrame rows before merge: {pre_merge_count}. Rows after merge: {df.shape[0]}"
        )

    log.info(f"Saving DataFrame to {output_file}")
    try:
        # csv_df = df.with_columns([pl.col("id").cast(str).alias("id_str")])

        df.write_parquet(file=output_file, use_pyarrow=True)

        return True

    except Exception as exc:
        log.error(exc)

        return False


def convert_pq_to_csv(
    input_pq: Path = RAW_PQ_PEOPLE_FILE,
    output_csv: Path = RAW_CSV_PEOPLE_FILE,
):
    """Load a Parquet file and save it as a CSV file."""
    if not input_pq:
        raise ValueError("Missing input Parquet file path")
    if not output_csv:
        raise ValueError("Missing output CSV file path")

    if not input_pq.exists():
        log.warning(f"Could not find input Parquet file at path: {input_pq}. Skipping.")
        return
    else:
        log.info(f"Loading existing Parquet file at path '{input_pq}' to DataFrame")
        try:
            df: pl.DataFrame = pl.read_parquet(input_pq, use_pyarrow=True)
        except Exception as exc:
            raise Exception(
                f"Unhandled exception reading .parquet file: {input_pq}. Details: {exc}"
            )

    if output_csv.exists():
        log.warning(f"Output CSV file exists at path '{output_csv}'. Loading CSV data")
        try:
            existing_data: pl.DataFrame = pl.read_csv(output_csv, dtypes=DF_DTYPES_MAP)
        except Exception as exc:
            raise Exception(
                f"Unhandled exception reading CSV data in path '{output_csv}' to DataFrame. Details: {exc}"
            )

    else:
        existing_data = None

    if existing_data is not None and not existing_data.is_empty():
        pre_merge_count: int = df.shape[0]
        try:
            df: pl.DataFrame = pl.concat([df, existing_data])
        except Exception as exc:
            raise Exception(
                f"Unhandled exception joining data into DataFrame. Details: {exc}"
            )

        log.debug(
            f"DataFrame rows before merge: {pre_merge_count}. Rows after merge: {df.shape[0]}"
        )

    log.info(f"Saving DataFrame to {output_csv}")
    try:
        # csv_df = df.with_columns([pl.col("id").cast(str).alias("id_str")])

        df.write_csv(file=output_csv)

        return True

    except Exception as exc:
        log.error(exc)

        return False
