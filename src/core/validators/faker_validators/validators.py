from faker import Faker


def validate_faker(fake: Faker = None, create_if_none: bool = False) -> Faker:
    """Validate a Faker instance.

    Params:
    -------

    fake (Faker): A Faker instance.
    create_if_none (bool): When True, the validator will initialize & return a Faker instance when the
        Faker object passed to this validator is None.
    """
    if fake is None:
        if create_if_none:
            fake: Faker = Faker()
        else:
            raise ValueError("Missing a Faker object to validate.")

    if not isinstance(fake, Faker):
        raise TypeError(
            f"Invalid type ({type(fake)}). Faker object must be of type faker.Faker."
        )

    return fake
