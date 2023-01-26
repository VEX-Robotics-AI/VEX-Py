"""Optical Sensor Gesture Types & Info."""


from collections.abc import Sequence
from dataclasses import dataclass
from enum import IntEnum, auto


__all__: Sequence[str] = 'GestureType', 'GestureInfo'


class GestureType(IntEnum):
    """Optical Sensor Gesture Types."""

    UP: int = auto()
    DOWN: int = auto()
    LEFT: int = auto()
    RIGHT: int = auto()


@dataclass
class GestureInfo:
    """Optical Sensor Gesture Info."""

    type: GestureType
