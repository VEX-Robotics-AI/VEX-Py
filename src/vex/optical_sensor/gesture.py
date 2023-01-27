"""Optical Sensor Gesture Types & Info."""


from collections.abc import Sequence
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import LiteralString


__all__: Sequence[LiteralString] = 'GestureType', 'GestureInfo'


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
