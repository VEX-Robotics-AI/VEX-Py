"""VEX Timer.

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_timer.html
"""


from collections.abc import Sequence
from typing import LiteralString, Self

from abm.decor import act, sense

from .units import TimeUnits

from .._util.doc import robotmesh_doc
from .._util.type import Num


__all__: Sequence[LiteralString] = ('Timer',)


@robotmesh_doc("""
    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_timer.html
""")
class Timer:
    """Timer."""

    def __init__(self: Self, /):
        """Initialize Timer."""

    def __eq__(self: Self, other: Self, /) -> bool:
        """Check equality."""
        return isinstance(other, type(self))

    def __hash__(self: Self, /) -> int:
        """Return integer hash."""
        return 0

    def __repr__(self: Self, /) -> LiteralString:
        """Return string representation."""
        return type(self).__name__

    @robotmesh_doc("""
        Sets the current value of the timer to 0
    """)
    @act
    def clear(self: Self, /) -> None:
        """Reset."""

    @robotmesh_doc("""
        Gets the current value of the timer in mS
    """)
    @sense
    def time(self: Self, timeUnits: TimeUnits = TimeUnits.MSEC, /) -> Num:
        """Get Timer's current value."""

    @robotmesh_doc("""
        Gets the current value of the system timer in mS

        Returns: value of the system timer in mS
    """)
    @sense
    @staticmethod
    def system() -> Num:
        """Get System's current time value."""
