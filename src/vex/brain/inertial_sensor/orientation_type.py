"""Orientation Types."""


from collections.abc import Sequence
from enum import IntEnum, auto

from ...util.doc import vexcode_doc


__all__: Sequence[str] = ('OrientationType',)


@vexcode_doc("""
    VEX IQ (2nd generation) Orientation Types.
""")
class OrientationType(IntEnum):
    """VEX IQ (2nd generation) Orientation Types."""

    # Pitch is the rotation around the side-to-side axis
    PITCH: int = auto()

    # Roll is the rotation around the front-to-back axis
    ROLL: int = auto()

    # Yaw is rotation around the vertical axis
    YAW: int = auto()
