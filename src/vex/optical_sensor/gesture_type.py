"""Optical Sensor Gesture Types."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('GestureType',)


class GestureType(IntEnum):
    """Optical Sensor Gesture Types."""

    UP: int = auto()
    DOWN: int = auto()
    LEFT: int = auto()
    RIGHT: int = auto()
