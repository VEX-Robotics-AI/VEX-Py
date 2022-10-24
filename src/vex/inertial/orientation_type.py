"""Orientation Types."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import vexcode_doc


__all__: Sequence[str] = ("OrientationType",)


@vexcode_doc(
    """VEX IQ (2nd generation) OrientationType types.
    """
)
class OrientationType(IntEnum):
    """VEX IQ (2nd generation) OrientationType types."""

    # Pitch is the rotation around the side to side axis,
    PITCH: int = 0

    # Roll is the rotation around the front to back axis.
    ROLL: int = 1

    # Yaw is rotation around the vertical axis.
    YAW: int = 2
