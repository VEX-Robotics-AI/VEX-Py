"""Timer."""


from collections.abc import Sequence

from __vex_decor import act, sense


__all__: Sequence[str] = ('Timer',)


class Timer:
    """Timer."""

    def __init__(self):
        """Create the Timer class, does not start the timer."""

    @act
    def reset(self):
        """Reset the time, clearing all data."""

    @act
    def start(self):
        """Start or resume timing the current lap."""

    @act
    def stop(self):
        """Stop or pause timing the current lap."""

    @act
    def start_lap(self):
        """Stop the current lap and starts a new one."""

    @sense
    def is_running(self) -> bool:
        """Return True if timer is currently running."""

    @sense
    def elapsed_time(self, lap_index: int = -1) -> float:
        """
        Return elapsed time for current lap (no args) or lap with given index.

        Negative indices (from the end) supported. Time in seconds.
        """

    @sense
    def lap_count(self) -> int:
        """Return number of laps stored (including the current one)."""

    @sense
    def total_time(self) -> float:
        """Return total elapsed time for all laps (time in seconds)."""

    @sense
    def average_time(self) -> float:
        """Return average time per lap (time in seconds)."""
