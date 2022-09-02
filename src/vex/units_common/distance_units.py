"""Distance Units."""


from collections.abc import Sequence
from enum import IntEnum

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('DistanceUnits',)


@robotmesh_doc("""
    The measurement units for distance values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_distance_units.html
""")
class DistanceUnits(IntEnum):
    """Distance Units."""

    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.
