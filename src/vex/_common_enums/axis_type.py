"""Inertial Axis Types."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS'


@robotmesh_doc("""
    Unit for inertial sensor axis

    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_axis_type.html
""")
class AxisType(IntEnum):
    """Inertial Axis Types."""

    # forward-to-backward movements
    XAXIS: int = 0

    # side-to-side movements
    YAXIS: int = 1

    # up-to-down movements
    ZAXIS: int = 2


# aliases
XAXIS: AxisType = AxisType.XAXIS
YAXIS: AxisType = AxisType.YAXIS
ZAXIS: AxisType = AxisType.ZAXIS
