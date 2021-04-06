from .abstract import Device


class Gyro(Device):
    ...


class GyroCalibrationType(Enum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2
