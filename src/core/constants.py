from pathlib import Path

DATA_DIR: Path = Path(".data")
RAW_DIR: Path = Path(f"{DATA_DIR}/raw")
OUTPUT_DIR: Path = Path(f"{DATA_DIR}/output")
OUTPUT_CSV_DIR: Path = Path(f"{OUTPUT_DIR}/csv")
OUTPUT_PQ_DIR: Path = Path(f"{OUTPUT_DIR}/parquet")
