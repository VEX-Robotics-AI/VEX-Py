"""V5 Device Types."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('V5DeviceType',)


@robotmesh_doc("""
    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_v5_device_type.html
""")
class V5DeviceType(IntEnum):
    """V5 Device Types."""

    NO_SENSOR: int = 0
    MOTOR: int = 2
    LED: int = 3
    ABS_ENC: int = 4
    BUMPER: int = 5
    IMU: int = 6
    RANGE: int = 7
    RADIO: int = 8
    TETHER: int = 9
    BRAIN: int = 10
    VISION: int = 11
    ADI: int = 12
    GYRO: int = 0x46
    SONAR: int = 0x47
    GENERIC: int = 128
    GENERIC_SERIAL: int = 129
    UNDEFINED = 255
