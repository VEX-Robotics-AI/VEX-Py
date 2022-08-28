"""Time Measurements."""


from collections.abc import Sequence
from enum import IntEnum

from abm.decor import act


__all__: Sequence[str] = 'TimeUnits', 'wait'


class TimeUnits(IntEnum):
    """The measurement units for time values."""

    SEC: int = 0   # A time unit that is measured in seconds.
    MSEC: int = 1   # A time unit that is measured in milliseconds.


# pylint: disable=unused-argument
@act
def wait(time: float, timeUnits: TimeUnits = TimeUnits.SEC):
    """
    Wait for a specific amount of time.

    Identical to sys.sleep().

    Parameters
    time: The length of time to wait
    timeUnits: The units of time (default seconds)
    """
