"""
Timer module.
"""


from __vex_decor import act, sense


class Timer:
    def __init__(self):
        """
        Create the Timer class, does not start the timer.
        """

    @act
    def reset(self):
        """
        Reset the time, clearing all data.
        """

    @act
    def start(self):
        """
        Start or resume timing the current lap.
        """

    @act
    def stop(self):
        """
        Stop or pause timing the current lap.
        """

    @act
    def start_lap(self):
        """
        Stops the current lap and starts a new one.
        """

    @sense
    def is_running(self) -> bool:
        """
        True if timer is currently running.
        """

    @sense
    def elapsed_time(self, lap_index: int = -1) -> float:
        """
        Elapsed time for the current lap (no args)
        or the lap with the given index.

        Negative indices (from the end) supported. Time in seconds.
        """

    @sense
    def lap_count(self) -> int:
        """
        Number of laps stored (including the current one).
        """

    @sense
    def total_time(self) -> float:
        """
        Total elapsed time for all laps.

        Time in seconds.
        """

    @sense
    def average_time(self) -> float:
        """
        Average time per lap.

        Time in seconds.
        """
