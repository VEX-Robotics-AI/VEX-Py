from __future__ import annotations

from typing import Any

from .abstract import Device


class Brain(Device):
    """
    Use the Brain class to see battery information, or write to the screen.
    """

    def __init__(self):
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id='CHECK')
        self._buttonUp: BrainButton = BrainButton(id='UP')
        self._buttonDown: BrainButton = BrainButton(id='DOWN')
        self._sound: BrainSound = BrainSound()

    @property
    def screen(self) -> BrainLcd:
        return self._screen

    @property
    def buttonCheck(self) -> BrainButton:
        return self._buttonCheck

    @property
    def buttonUp(self) -> BrainButton:
        return self._buttonUp

    @property
    def buttonDown(self) -> BrainButton:
        return self._buttonDown

    @property
    def sound(self) -> BrainSound:
        return self._sound


class BrainButton:
    """
    Use the button class to get values from the brain's buttons.
    """

    def __init__(self, id: Any):
        self._id: Any = id
        self._pressing: bool = False

    def pressing(self) -> bool:
        """
        Gets the pressed status of a button.

        Returns
        True if pressed, False otherwise.
        """
        return self._pressing


class BrainLcd:
    """
    Use this class to write or draw to the brain's LCD screen.
    * 21 characters wide
    * 5 lines (1-5)
    """

    def print_line(self, number: int, text: str):
        """
        Prints a number, string, or boolean at a particular line,
        clearing the rest of the line.

        Parameters
        number: Line to print on, 1 is top line.
        text: object to print, usually a string.
              Use "" to clear the line.
              For multiple arguments, use format like
              "x: %g y: %g" % (x, y) -> "x: 123 y: 456"
              Supported format flags are g (all) x (hex) d (int) f (float)
        """
        return ('print_line', {'number': number, 'text': text})

    def clear_screen(self):
        """
        Clears the whole screen.
        """
        return ('clear_screen',)


class BrainSound:
    ...