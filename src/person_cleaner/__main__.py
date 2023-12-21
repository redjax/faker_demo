from __future__ import annotations

import sys

sys.path.append(".")

from person_cleaner import run_cleaning_operations

from loguru import logger as log
from red_utils.ext.loguru_utils import LoguruSinkStdOut, init_logger

if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])

    log.info(f"Person cleaner start")

    run_cleaning_operations()
