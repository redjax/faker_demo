from __future__ import annotations

from pathlib import Path

from core.constants import DATA_DIR, OUTPUT_CSV_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR, RAW_DIR

CLEANED_PQ_FILE: Path = Path(f"{OUTPUT_PQ_DIR}/people_cleaned.parquet")
CLEANED_CSV_FILE: Path = Path(f"{OUTPUT_CSV_DIR}/people_cleaned.csv")
