"""Time units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'TimeUnits', 'SECONDS', 'MSEC', '_Time'


@robotmesh_doc("""
    Measurement units for time values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_time_units.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_time_units.html
""")
class TimeUnits(IntEnum):
    """Time units."""

    SEC: int = 0  # time unit measured in Seconds
    MSEC: int = 1  # time unit measured in Milliseconds


# aliases
SECONDS: TimeUnits = TimeUnits.SEC
MSEC: TimeUnits = TimeUnits.MSEC


class _Time(_MeasurementWithUnitABC):
    unit: TimeUnits = SECONDS
