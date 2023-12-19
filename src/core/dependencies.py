from faker import Faker


def new_faker(seed: int | None = None) -> Faker:
    """Generate a new Faker object, with an optional seed value.

    Params:
    -------
    - seed (int|None): An optional integer to be used as a data seed for Faker.
        The same seed will produce the same fake data each time it is used,
        which is beneficial for testing.
    """
    fake: Faker = Faker()

    if seed is not None:
        if not isinstance(seed, int):
            raise TypeError(
                f"Invalid type for seed: {type(seed)}. Must be of type int."
            )
        Faker.seed(seed)

    return fake


DEFAULT_FAKER: Faker = new_faker()
