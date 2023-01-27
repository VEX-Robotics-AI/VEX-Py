"""Optical Sensor LED State Type."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString


__all__: Sequence[LiteralString] = ('LedStateType',)


class LedStateType(IntEnum):
    """Optical Sensor LED State Type."""

    ON: int = auto()
    OFF: int = auto()
