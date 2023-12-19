from pydantic import BaseModel, Field, field_validator, ValidationError

from .base import CharacterBase


class Character(CharacterBase):
    pass
