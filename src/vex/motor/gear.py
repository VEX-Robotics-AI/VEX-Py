"""Motor Gear Settings."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('GearSetting',)


@robotmesh_doc("""
    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_gear_setting.html
""")
class GearSetting(IntEnum):
    """Motor Gear Settings."""

    # unit representing gear setting for stock gears (red) (max rpm = 100)
    RATIO_36_1 = RATIO36_1 = 0

    # unit representing gear setting for upgraded gears (green) (max rpm = 200)
    RATIO_18_1 = RATIO18_1 = 1

    # unit representing gear setting for upgraded gears (blue) (max rpm = 600)
    RATIO_6_1 = RATIO6_1 = 2
