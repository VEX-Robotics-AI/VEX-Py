"""Timer.

Robot Mesh VEX IQ Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacetimer.html

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/namespacetimer.html
"""


from collections.abc import Sequence
from typing import LiteralString, Self

from abm.decor import act, sense

from vex._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('Timer',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classtimer_1_1_timer.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classtimer_1_1_timer.html
""")
class Timer:
    """Timer."""

    @robotmesh_doc("""
        Create the Timer class, does not start the timer
    """)
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
        Reset the time, clearing all data
    """)
    @act
    def reset(self: Self, /):
        """Reset."""

    @robotmesh_doc("""
        Start or resume timing the current lap
    """)
    @act
    def start(self: Self, /):
        """Start or resume."""

    @robotmesh_doc("""
        Stop or pause timing the current lap
    """)
    @act
    def stop(self: Self, /):
        """Stop or pause."""

    @robotmesh_doc("""
        Stops the current lap and starts a new one
    """)
    @act
    def start_lap(self: Self, /):
        """Start new lap."""

    @robotmesh_doc("""
        True if timer is currently running
    """)
    @sense
    def is_running(self: Self, /) -> bool:
        """Check if Timer is running."""

    @robotmesh_doc("""
        Elapsed time for current lap (no args) or lap with given index.

        Negative indices (from the end) supported. Time in seconds.
    """)
    @sense
    def elapsed_time(self: Self, lap_index: int = -1, /) -> float:
        """Return elapsed time."""

    @robotmesh_doc("""
        Number of laps stored (including the current one)
    """)
    @sense
    def lap_count(self: Self, /) -> int:
        """Return number of laps."""

    @robotmesh_doc("""
        Total elapsed time for all laps

        Time in seconds
    """)
    @sense
    def total_time(self: Self, /) -> float:
        """Return total time."""

    @robotmesh_doc("""
        Average time per lap

        Time in seconds
    """)
    @sense
    def average_time(self: Self, /) -> float:
        """Return average time per lap."""
