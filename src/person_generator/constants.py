from pathlib import Path

import pendulum
import polars as pl

CSV_DTYPES_MAP: dict = {
    "dob": pendulum.Date,
    "age": int,
}

DF_DTYPES_MAP: dict = {
    "id": pl.Object,
}
