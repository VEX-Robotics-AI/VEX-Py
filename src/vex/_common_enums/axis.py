"""Inertial Axis Types."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS'


@robotmesh_doc("""
    Unit for inertial sensor axis

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_axis_type.html
""")
class AxisType(IntEnum):
    """Inertial Axis Types."""

    XAXIS: int = 0  # forward-to-backward movements
    YAXIS: int = 1  # side-to-side movements
    ZAXIS: int = 2  # up-to-down movements


# aliases
XAXIS: AxisType = AxisType.XAXIS
YAXIS: AxisType = AxisType.YAXIS
ZAXIS: AxisType = AxisType.ZAXIS
