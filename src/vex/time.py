"""Time."""


from collections.abc import Sequence
from enum import IntEnum

from abm.decor import act

# pylint: disable=unused-import
from .util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = 'TimeUnits', 'wait'


@robotmesh_doc("""
    The measurement units for time values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_time_units.html
""")
class TimeUnits(IntEnum):
    """Time Units."""

    SEC: int = 0   # A time unit that is measured in seconds.
    MSEC: int = 1   # A time unit that is measured in milliseconds.


# pylint: disable=unused-argument
@robotmesh_doc("""
    Wait for a specific amount of time.

    Identical to sys.sleep().

    Parameters
    time: The length of time to wait
    timeUnits: The units of time (default seconds)

    robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html#a6b9ca2db773bef3a3569a0d6b22f2749
""")
@act
def wait(time: float, timeUnits: TimeUnits = TimeUnits.SEC):
    """Wait."""
