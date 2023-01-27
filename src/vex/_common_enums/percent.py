"""Percentage unit."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'PercentUnits', 'PERCENT'


@robotmesh_doc("""
    Unit of Percentage.

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_percent_units.html
""")
class PercentUnits(IntEnum):
    """Percentage unit."""

    PCT: int = 0  # unit type representing values from 0% to 100%


# aliases
PERCENT = PercentUnits.PCT
