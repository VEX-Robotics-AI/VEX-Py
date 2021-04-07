from enum import IntEnum

from __decor import act, sense

from .abstract import Device


class Gyro(Device):
    ...


class GyroCalibrationType(IntEnum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2
