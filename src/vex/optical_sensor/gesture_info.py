"""Optical Sensor Gesture Info."""


from collections.abc import Sequence
from dataclasses import dataclass

from .gesture_type import GestureType


__all__: Sequence[str] = ('GestureInfo',)


@dataclass
class GestureInfo:
    """Optical Sensor Gesture Info."""

    type: GestureType
