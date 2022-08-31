"""Brain LCD Screen."""


from abm.decor import act

from .._abstract import SingletonDevice


class BrainLcd(SingletonDevice):
    """
    Use this class to write or draw to the brain's LCD screen.

    * 21 characters wide
    * 5 lines (1-5)
    """

    @act
    def print_line(self, number: int, text: str):
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

    @act
    def clear_screen(self):
        """Clear the whole screen."""
