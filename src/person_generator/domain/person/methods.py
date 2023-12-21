from faker import Faker

from core.validators.faker_validators import validate_faker
from .schemas import Person

from red_utils.ext.context_managers import SimpleSpinner

from loguru import logger as log

from uuid import uuid4


def generate_random_person(fake: Faker = None) -> Person:
    """Generate fake data with Faker and populate a Person object."""
    fake = validate_faker(fake)

    try:
        person = Person()

        person.id = str(uuid4())
        person.first_name = fake.first_name()
        person.last_name = fake.last_name()
        person.dob = fake.date_of_birth(minimum_age=1, maximum_age=110)
        person.email = f"{fake.user_name()}@{fake.free_email_domain()}"
        person.phone = fake.phone_number()
        person.job = fake.job()
        person.company = fake.company()
        person.license = fake.license_plate()
        person.vin = fake.vin()
        person.addr_housenum = int(fake.building_number())
        person.addr_street = fake.street_address()
        person.addr_city = fake.city()
        person.addr_state = fake.country_code()
        person.addr_zip = str(fake.postcode())
        person.addr_country = fake.country()

        return person

    except Exception as exc:
        raise Exception(
            f"Unhandled exception generating Person instance with Faker. Details: {exc}"
        )


def generate_people(fake: Faker = None, num: int = 3) -> list[Person]:
    """Generate multiple Person instances at once."""
    ## Variable to control whether or not a CLI spinner is displayed for longer operations
    use_spinner = False

    def _generate(fake=fake, num=num) -> list[Person]:
        people: list[Person] = []
        count: int = 0

        while count < num:
            person: Person = generate_random_person(fake=fake)
            # log.debug(f"Person: {person}, Age: {person.age}")

            people.append(person)

            count += 1

        return people

    if num >= 5000 and num < 10000:
        log.warning(
            f"Generating more than {num} Person records may be a slow operation on some hardware."
        )
        use_spinner = True

    if num >= 10000 and num < 50000:
        log.warning(f"Generating more than 10000 Person records is a slow operation.")
        use_spinner = True

    if num >= 50000:
        log.warning(f"Generating more than 50000 Person records will take a while.")
        use_spinner = True

    fake = validate_faker(fake)

    if use_spinner:
        with SimpleSpinner(f"Generating [{num}] Person objects... "):
            people = _generate()
    else:
        people = _generate()

    log.debug(f"Generated [{len(people)}] Person object(s).")

    return people
