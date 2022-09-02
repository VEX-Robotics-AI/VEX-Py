"""Time Units."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = ('TimeUnits',)


@robotmesh_doc("""
    The measurement units for time values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_time_units.html
""")
class TimeUnits(IntEnum):
    """Time Units."""

    SEC: int = 0   # A time unit that is measured in seconds.
    MSEC: int = 1   # A time unit that is measured in milliseconds.
