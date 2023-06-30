"""Analog units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .percent import PERCENT

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('AnalogUnits',)


@robotmesh_doc("""
    Analog units

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_analog_units.html
""")
class AnalogUnits(IntEnum):
    """Analog units."""

    PCT: int = PERCENT  # analog unit representing values from 0% to 100%
    RANGE_8BIT: int = 1  # analog unit on an 8-bit range
    RANGE_10BIT: int = 2  # analog unit on a 10-bit range
    RANGE_12BIT: int = 3  # analog unit on a 12-bit range
    MV: int = 4  # milivolt unit
