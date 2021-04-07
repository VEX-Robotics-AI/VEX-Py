from __decor import return_qualname_and_args

from .abstract import Device, Enum


class FadeType(Enum):
    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2


@return_qualname_and_args
class Touchled(Device):
    """
    Use this class when programming with the touch LED device.
    """
