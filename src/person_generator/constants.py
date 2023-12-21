from pathlib import Path

import pendulum
import polars as pl

CSV_DTYPES_MAP: dict = {
    "dob": pendulum.Date,
    "age": int,
    "addr_housenum": int,
    "addr_zip": str,
}

DF_DTYPES_MAP: dict = {"id": str, "dob": pendulum.Date, "age": int, "addr_zip": str}
