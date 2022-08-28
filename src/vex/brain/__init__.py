"""VEX Brain."""


from __future__ import annotations

from collections.abc import Sequence
from typing_extensions import Self   # pylint: disable=no-name-in-module

from abm.decor import act, sense

from ..abstract import SingletonDevice
from ..time import TimeUnits
from .sound import NoteType


__all__: Sequence[str] = (
    'Brain',
    'BrainButton',
    'BrainLcd',
    'BrainSound',
    'NoteType',
)


class Brain(SingletonDevice):
    """Use the Brain class to see battery information, or write to the screen."""   # noqa: E501

    def __init__(self):
        """Initialize Brain."""
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id='CHECK')
        self._buttonUp: BrainButton = BrainButton(id='UP')
        self._buttonDown: BrainButton = BrainButton(id='DOWN')
        self._sound: BrainSound = BrainSound()

    @property
    def screen(self) -> BrainLcd:
        """Brain LCD."""
        return self._screen

    @property
    def buttonCheck(self) -> BrainButton:
        """Brain Button CHECK."""
        return self._buttonCheck

    @property
    def buttonUp(self) -> BrainButton:
        """Brain Button UP."""
        return self._buttonUp

    @property
    def buttonDown(self) -> BrainButton:
        """Brain Button DOWN."""
        return self._buttonDown

    @property
    def sound(self) -> BrainSound:
        """Brain Sound."""
        return self._sound


class BrainButton:
    """Use the button class to get values from the brain's buttons."""

    def __init__(self, id: str):   # pylint: disable=redefined-builtin
        """Initialize BrainButton."""
        self.id: str = id

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, BrainButton) and (other.id == self.id)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash(self.id)

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.id})'

    @sense
    def pressing(self) -> bool:
        """
        Get the pressed status of a button.

        Returns
        True if pressed, False otherwise.
        """


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
