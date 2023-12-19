import sys

sys.path.append(".")

from faker import Faker
from loguru import logger as log
import polars as pl

from red_utils.ext.loguru_utils import init_logger, LoguruSinkStdOut

from core.dependencies import new_faker, DEFAULT_FAKER


def main(fake: Faker = None):
    if fake is None:
        fake = Faker()

    print(fake.name())


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])
    log.info("Start Fake person database.")

    ## Uses the global faker initialized at app start
    default_fake = DEFAULT_FAKER
    ## New data each time
    fake = new_faker()
    ## Same data each time
    fake_static = new_faker(seed=142356893021)

    main(fake)
