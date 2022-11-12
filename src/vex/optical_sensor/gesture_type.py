"""Gesture Types."""

from collections.abc import Sequence
from enum import IntEnum, auto

from ..util.doc import vexcode_doc


__all__: Sequence[str] = 'GestureType'


@vexcode_doc("""
    VEX Optical Sensor Gesture Type.
""")
class GestureType(IntEnum):
    """VEX Optical Sensor Gesture Type."""

    UP: int = auto()
    DOWN: int = auto()
    LEFT: int = auto()
    RIGHT: int = auto()
