"""Timer."""


from collections.abc import Sequence

from abm.decor import act, sense

from .._abstract_device import SingletonDevice
from ..time.time_units import TimeUnits

from .._util.doc import vexcode_doc


__all__: Sequence[str] = ('BrainTimer',)


class BrainTimer(SingletonDevice):
    """Timer."""

    @vexcode_doc("""
        Reset Timer

        Resets the IQ Brain's timer.

        The Brain's timer begins at the beginning of each project.
        The Reset Timer command can be used to reset the timer value
        back to 0 seconds.
    """)
    @act
    def clear(self):
        """Reset."""

    @vexcode_doc("""
        Timer Value

        Reports the value of the IQ Brain's timer.

        The timer starts at 0 seconds when the program starts,
        and reports the timer's value as a decimal value.

        The UNITS parameter accepts either SECONDS or MSEC (milliseconds)
        as a valid argument.
    """)
    @sense
    def time(self, unit: TimeUnits) -> float:
        """Return elapsed time."""

    @vexcode_doc("""
        Timer Event

        Runs the specified callback function
        when the IQ Brain's timer is greater than the specified time value.

        The IQ Brain's timer begins at the start of each program.

        The Timer Event function takes 2 parameters.

        The first is the callback function parameter.
        A function will need to be created to pass to the Timer Event function.

        The second parameter is the time at which the function will run.
        The callback function will run once the IQ Brain's timer is greater
        than the passed value. The amount of time should be in milliseconds.

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    @act
    def event(self, callback: callable, msecs: int, /):
        """Trigger callback function after specified number of miliseconds."""
