from __future__ import annotations

import sys

sys.path.append(".")

from core.constants import DATA_DIR, OUTPUT_CSV_DIR, OUTPUT_DIR, OUTPUT_PQ_DIR, RAW_DIR
from core.dependencies import new_faker
from person_generator.main import generate_main
from person_cleaner import CLEANED_CSV_FILE, CLEANED_PQ_FILE
from person_cleaner import run_cleaning_operations

from faker import Faker
from loguru import logger as log

from red_utils.ext.loguru_utils import LoguruSinkStdOut, init_logger

## Skip all prompts while debugging
DBG_SKIP_PROMPTS: bool = True

DEFAULT_SEED = None
DEFAULT_COUNT = 1000
SAVE_CSV: bool = True


if __name__ == "__main__":
    init_logger(sinks=[LoguruSinkStdOut(level="DEBUG").as_dict()])
    log.info(f"Starting random Person generator")

    if DBG_SKIP_PROMPTS:
        skip_prompts = True
    else:
        prompt_use_defaults: str = input(
            f"Defaults: [seed: {DEFAULT_SEED}], [person_count: {DEFAULT_COUNT}]\n\t| Skip prompts and use defaults? (Y/N) default=N : "
        )

        match prompt_use_defaults.upper():
            case "Y":
                log.info("Setting skip_prompts=True")
                skip_prompts: bool = True
            case "N":
                log.info("Setting skip_prompts=False")
                skip_prompts: bool = False
            case ["", None]:
                log.warning("Your answer was empty, setting skip_prompts=False")
                skip_prompts = False
            case _:
                log.error(
                    f"Invalid choice: [{prompt_use_defaults}], settings skip_prompts=False"
                )
                skip_prompts: bool = False

    log.info(f"Creating Faker object")

    if skip_prompts:
        faker_seed = None

    else:
        prompt_faker_seed = input("Provide a seed for Faker? (Y/N) default=N: ")
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
            case _:
                msg = ValueError(f"Invalid option: {prompt_faker_seed}")
                log.error(msg)
                exit(1)

    fake: Faker = new_faker(seed=faker_seed)

    if skip_prompts:
        num: int = DEFAULT_COUNT

    else:
        prompt_num = input("How many Person objects do you want to generate? ")
        try:
            num: int = int(prompt_num)
        except TypeError as type_err:
            raise TypeError(
                f"Unable to convert type ({type(prompt_num)}) to int. Details: {type_err}"
            )

    log.info(f"Generating {num} Person objects!")
    people = generate_main(fake=fake, num_people=num, save_csv=SAVE_CSV)

    log.info(f"Running Person data cleaner & saving output to {CLEANED_PQ_FILE}")
    try:
        run_cleaning_operations(save_csv=SAVE_CSV)
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception running Person cleaning operations. Details: {exc}"
        )
        log.error(msg)

        raise msg
