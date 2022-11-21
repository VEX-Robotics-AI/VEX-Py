"""Touch LED Colors."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('Color',)


class Color(IntEnum):
    """Touch LED Colors."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = auto()
    YELLOW = auto()
    ORANGE = auto()
    PURPLE = auto()
    RED_VIOLET = auto()
    VIOLET = auto()
    BLUE_VIOLET = auto()
    BLUE_GREEN = auto()
    YELLOW_GREEN = auto()
    YELLOW_ORANGE = auto()
    RED_ORANGE = auto()
