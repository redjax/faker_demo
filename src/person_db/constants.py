from pathlib import Path

import pendulum

DATA_DIR: Path = Path("person_db/.data")
RAW_DIR: Path = Path(f"{DATA_DIR}/raw")

DF_DTYPES_MAP: dict = {"dob": pendulum.Date}
