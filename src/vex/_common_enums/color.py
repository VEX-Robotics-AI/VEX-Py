"""Colors."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'Color', 'ColorHue'


@robotmesh_doc("""
    Defined color hue values.

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_color_hue.html
""")
class Color(IntEnum):
    """Colors."""

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
    PURPLE: int = auto()
    BLACK: int = auto()


# alias
ColorHue = Color
