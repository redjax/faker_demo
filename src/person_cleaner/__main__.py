import sys

sys.path.append(".")

from red_utils.ext.loguru_utils import init_logger, LoguruSinkStdOut
from loguru import logger as log

from person_cleaner import run_cleaning_operations


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])

    log.info(f"Person cleaner start")

    run_cleaning_operations()
