"""Optical Sensor LED State Type."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('LedStateType',)


class LedStateType(IntEnum):
    """Optical Sensor LED State Type."""

    ON: int = auto()
    OFF: int = auto()
