from __future__ import annotations

from pathlib import Path

import pendulum
import polars as pl

from core.constants import DATA_DIR, RAW_DIR, OUTPUT_CSV_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR

CSV_DTYPES_MAP: dict = {
    "dob": pendulum.Date,
    "age": int,
    "addr_housenum": int,
    "addr_zip": str,
}

DF_DTYPES_MAP: dict = {"id": str, "dob": pendulum.Date, "age": int, "addr_zip": str}

RAW_CSV_PEOPLE_FILE: Path = Path(f"{RAW_DIR}/people.csv")
RAW_PQ_PEOPLE_FILE: Path = Path(f"{RAW_DIR}/people.parquet")
