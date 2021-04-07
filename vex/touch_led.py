from enum import IntEnum

from __decor import act, sense

from .abstract import Device


class FadeType(IntEnum):
    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2


class Touchled(Device):
    """
    Use this class when programming with the touch LED device.
    """
