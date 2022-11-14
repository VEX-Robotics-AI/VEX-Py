"""Timer.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacetimer.html
"""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import act, sense

from vex.util.doc import robotmesh_doc


__all__: Sequence[str] = ('Timer',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classtimer_1_1_timer.html
""")
class Timer:
    """Timer."""

    @robotmesh_doc("""
        Create the Timer class, does not start the timer.
    """)
    def __init__(self):
        """Initialize Timer."""

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, type(self))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return 0

    def __repr__(self) -> str:
        """Return String Representation."""
        return type(self).__name__

    @robotmesh_doc("""
        Reset the time, clearing all data.
    """)
    @act
    def reset(self):
        """Reset Timer."""

    @robotmesh_doc("""
        Start or resume timing the current lap.
    """)
    @act
    def start(self):
        """Start or Resume Timer."""

    @robotmesh_doc("""
        Stop or pause timing the current lap.
    """)
    @act
    def stop(self):
        """Stop or Pause Timer."""

    @robotmesh_doc("""
        Stop the current lap and starts a new one.
    """)
    @act
    def start_lap(self):
        """Start New Timer Lap."""

    @robotmesh_doc("""
        Return True if timer is currently running.
    """)
    @sense
    def is_running(self) -> bool:
        """Check if Timer is running."""

    @robotmesh_doc("""
        Return elapsed time for current lap (no args) or lap with given index.

        Negative indices (from the end) supported. Time in seconds.
    """)
    @sense
    def elapsed_time(self, lap_index: int = -1, /) -> float:
        """Return Elapsed Time."""

    @robotmesh_doc("""
        Return number of laps stored (including the current one).
    """)
    @sense
    def lap_count(self) -> int:
        """Return Number of Laps."""

    @robotmesh_doc("""
        Return total elapsed time for all laps (time in seconds).
    """)
    @sense
    def total_time(self) -> float:
        """Return Total Time."""

    @robotmesh_doc("""
        Return average time per lap (time in seconds).
    """)
    @sense
    def average_time(self) -> float:
        """Return Average Time per Lap."""
