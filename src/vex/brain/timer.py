"""VEX Brain Timer."""


from typing_extensions import Self

from abm.decor import act, sense
from vex.util.doc import vexcode_doc


@vexcode_doc("""VEX brain.timer""")
class BrainTimer:
    """Timer."""

    @vexcode_doc(
        """
        Create the BrainTimer class.
    """
    )
    def __init__(self):
        """Initialize Timer."""

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, type(self))

    def __hash__(self) -> int:
        """Return integer hash."""
        return 0

    def __repr__(self) -> str:
        """Return String Representation."""
        return type(self).__name__

    @vexcode_doc(
        """Resets the IQ Brain's timer.

        The Brain's timer begins at the beginning of each project.
        The Reset Timer command can be used to reset the timer value back to 0 seconds."""
    )
    @act
    def clear(self):
        """Resets the IQ Brain's timer."""

    @vexcode_doc(
        """Reports the value of the IQ Brain's timer.
            brain.timer.time(UNITS)
        The timer starts at 0 seconds when the program starts, and reports the timer's value as a decimal value.
        The UNITS parameter accepts either SECONDS or MSEC (milliseconds) as a valid argument."""
    )
    @sense
    def time(self, units) -> float:
        """Reports the value of the IQ Brain's timer."""
