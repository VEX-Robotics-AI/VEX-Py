"""
Timer module.
"""


from __decor import return_qualname_and_args


@return_qualname_and_args
class Timer:
    def __init__(self):
        """
        Create the Timer class, does not start the timer.
        """

    def reset(self):
        """
        Reset the time, clearing all data.
        """

    def start(self):
        """
        Start or resume timing the current lap.
        """

    def stop(self):
        """
        Stop or pause timing the current lap.
        """

    def start_lap(self):
        """
        Stops the current lap and starts a new one.
        """

    def is_running(self) -> bool:
        """
        True if timer is currently running.
        """

    def elapsed_time(self, lap_index: int = -1) -> float:
        """
        Elapsed time for the current lap (no args)
        or the lap with the given index.

        Negative indices (from the end) supported. Time in seconds.
        """

    def lap_count(self) -> int:
        """
        Number of laps stored (including the current one).
        """

    def total_time(self) -> float:
        """
        Total elapsed time for all laps.

        Time in seconds.
        """

    def average_time(self) -> float:
        """
        Average time per lap.

        Time in seconds.
        """
