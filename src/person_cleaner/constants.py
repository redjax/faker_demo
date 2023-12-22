from pathlib import Path

from core.constants import OUTPUT_DIR, DATA_DIR, RAW_DIR, OUTPUT_CSV_DIR, OUTPUT_PQ_DIR

CLEANED_PQ_FILE: Path = Path(f"{OUTPUT_PQ_DIR}/people_cleaned.parquet")
CLEANED_CSV_FILE: Path = Path(f"{OUTPUT_CSV_DIR}/people_cleaned.csv")
