from __future__ import annotations

from .base import CharacterBase

from pydantic import BaseModel, Field, ValidationError, field_validator


class Character(CharacterBase):
    pass
