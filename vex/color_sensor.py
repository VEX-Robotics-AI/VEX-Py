from __decor import return_qualname_and_args

from .abstract import Device, Enum


class ColorHue(Enum):
    """
    Defined color hue values.
    """
    NONE: int = 0
    RED: int = 1
    RED_ORANGE: int = 2
    ORANGE: int = 3
    YELLOW_ORANGE: int = 4
    YELLOW: int = 5
    YELLOW_GREEN: int = 6
    GREEN: int = 7
    BLUE_GREEN: int = 8
    BLUE: int = 9
    BLUE_VIOLET: int = 10
    VIOLET: int = 11
    RED_VIOLET: int = 12
    WHITE: int = 13


@return_qualname_and_args
class Colorsensor(Device):
    ...
