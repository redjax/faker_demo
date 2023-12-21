import sys

sys.path.append(".")

from core.constants import DATA_DIR, RAW_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR, OUTPUT_CSV_DIR
from core.dependencies import new_faker

from faker import Faker
from loguru import logger as log
from red_utils.ext.loguru_utils import init_logger, LoguruSinkStdOut

from person_generator.main import generate_main

if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])
    log.info(f"Starting random Person generator")

    log.info(f"Creating Faker object")

    prompt_faker_seed = input("Provide a seed for Faker? (Y/N): ")
    match prompt_faker_seed.upper():
        case "Y":
            faker_seed: str = input("Input an integer seed below:\n> ")
            try:
                faker_seed: int = int(faker_seed)
            except TypeError as type_err:
                raise TypeError(
                    f"Unable to convert type ({type(faker_seed)}) to int. Details: {type_err}"
                )
            log.info(f"Will use Faker seed: {faker_seed}")
        case "N":
            log.info("Ok, skipping seed")
            faker_seed = None

    fake: Faker = new_faker(seed=faker_seed)

    prompt_num = input("How many Person objects do you want to generate? ")
    try:
        prompt_num: int = int(prompt_num)
    except TypeError as type_err:
        raise TypeError(
            f"Unable to convert type ({type(prompt_num)}) to int. Details: {type_err}"
        )

    log.info(f"Generating {prompt_num} Person objects!")
    people = generate_main(fake=fake, num_people=prompt_num)
