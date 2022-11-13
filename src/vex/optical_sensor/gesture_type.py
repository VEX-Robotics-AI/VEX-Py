"""Optical Sensor Gesture Types."""


from __future__ import annotations

from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('GestureType',)


class GestureType(IntEnum):
    """Optical Sensor Gesture Types."""

    UP: int = auto()
    DOWN: int = auto()
    LEFT: int = auto()
    RIGHT: int = auto()

    @property
    def type(self) -> GestureType:
        """Return Gesture Type."""
        return self
