"""Brain LCD Screen."""


from collections.abc import Sequence

from abm.decor import act

from .._abstract_device import SingletonDevice
from ..util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = ("BrainLcd",)


# TODO: add VEXcode features
@robotmesh_doc(
    """
    Use this class to write or draw to the brain's LCD screen.

    * 21 characters wide
    * 5 lines (1-5)

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain_lcd.html
"""
)
class BrainLcd(SingletonDevice):
    """Brain LCD Screen."""

    @robotmesh_doc(
        """
        Print a number, string, or boolean at a particular line.

        (clearing the rest of the line)

        Parameters
        number: Line to print on, 1 is top line.
        text: object to print, usually a string.
              Use "" to clear the line.
              For multiple arguments, use format like
              "x: %g y: %g" % (x, y) -> "x: 123 y: 456"
              Supported format flags are g (all) x (hex) d (int) f (float)
    """
    )
    @act
    def print_line(self, number: int, text: str, /):
        """Print to a line on Brain LCD Screen."""

    @robotmesh_doc(
        """
        Clear the whole screen.
    """
    )
    @vexcode_doc(
        """
        Clears the entire VEX IQ Brain's Screen.

        Clear Screen will not reset the Brain's screen cursor.

        Use the Set Cursor command to set the Brain's cursor
        to the desired position.
    """
    )
    @act
    def clear_screen(self):
        """Clear Brain LCD Screen."""

    @vexcode_doc(
        """
        Set the cursor location for Brain's Print commands.

        brain.screen.set_cursor(ROW, COL).
    """
    )
    @act
    def set_cursor(self, row, col):
        """Set the cursor location for Brain's Print commands."""
