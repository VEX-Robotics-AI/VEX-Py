from __decor import return_qualname_and_args

from .abstract import Device, Enum


@return_qualname_and_args
class Gyro(Device):
    ...


class GyroCalibrationType(Enum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2
