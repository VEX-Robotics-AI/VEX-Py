"""VEX Optical Sensor LED State Type."""

from collections.abc import Sequence
from enum import IntEnum, auto

from ..util.doc import vexcode_doc


__all__: Sequence[str] = 'LedStateType'


@vexcode_doc("""
    VEX Optical Sensor LED State Type.
""")
class LedStateType(IntEnum):
    """VEX Optical Sensor LED State Type."""

    ON: int = auto()
    OFF: int = auto()
