"""Gyro calibration types."""


from collections.abc import Sequence
from enum import IntEnum, auto

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = ('GyroCalibrationType',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_gyro_calibration_type.html
""")
class GyroCalibrationType(IntEnum):
    """Gyro calibration types."""

    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2
    NORMAL: int = auto()
    EXTENDED: int = auto()
