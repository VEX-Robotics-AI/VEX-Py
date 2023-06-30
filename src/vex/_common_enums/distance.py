"""Distance units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'DistanceUnits', 'MM', 'INCHES', '_Distance'


@robotmesh_doc("""
    The measurement units for distance values.

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_distance_units.html
""")
class DistanceUnits(IntEnum):
    """Distance units."""

    MM: int = 0  # distance unit measured in Millimeters
    IN: int = 1  # distance unit measured in Inches
    CM: int = 2  # distance unit measured in Centimeters


# aliases
MM: DistanceUnits = DistanceUnits.MM
INCHES: DistanceUnits = DistanceUnits.IN


class _Distance(_MeasurementWithUnitABC):
    unit: DistanceUnits = MM
