"""Time units."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'TimeUnits', 'SECONDS', 'MSEC'


@robotmesh_doc("""
    The measurement units for time values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_time_units.html
""")
class TimeUnits(IntEnum):
    """Time units."""

    SEC: int = 0   # time unit measured in Seconds
    MSEC: int = 1   # time unit measured in Milliseconds


# aliases
SECONDS: TimeUnits = TimeUnits.SEC
MSEC: TimeUnits = TimeUnits.MSEC
