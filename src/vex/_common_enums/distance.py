"""Distance units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'DistanceUnits', 'MM', 'INCHES'


@robotmesh_doc("""
    The measurement units for distance values.

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_distance_units.html
""")
class DistanceUnits(IntEnum):
    """Distance units."""

    MM: int = 0   # distance unit measured in Millimeters
    IN: int = 1   # distance unit measured in Inches
    CM: int = 2   # distance unit measured in Centimeters


# aliases
MM: DistanceUnits = DistanceUnits.MM
INCHES: DistanceUnits = DistanceUnits.IN
