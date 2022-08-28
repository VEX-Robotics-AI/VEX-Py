"""VEX Color Sensor."""


from collections.abc import Sequence
from enum import IntEnum
from typing_extensions import Self   # pylint: disable=no-name-in-module

from abm.decor import act, sense

from .abstract import Device
from .port import Ports


__all__: Sequence[str] = 'ColorHue', 'Colorsensor'


class ColorHue(IntEnum):
    """Defined color hue values."""

    NONE: int = 0
    RED: int = 1
    RED_ORANGE: int = 2
    ORANGE: int = 3
    YELLOW_ORANGE: int = 4
    YELLOW: int = 5
    YELLOW_GREEN: int = 6
    GREEN: int = 7
    BLUE_GREEN: int = 8
    BLUE: int = 9
    BLUE_VIOLET: int = 10
    VIOLET: int = 11
    RED_VIOLET: int = 12
    WHITE: int = 13


class Colorsensor(Device):
    """VEX Color Sensor."""

    def __init__(
            self, index: Ports,
            is_grayscale: bool = False,
            proximity: float = 700):
        """
        Create new color sensor object on the port specified in the parameter.

        Parameters:
        - index: The port index (zero-based)
        - is_grayscale: Whether grayscale mode (LED on), default false
        - proximity: threshold (default 700)
        """
        self.port: Ports = index
        self.is_grayscale: bool = is_grayscale
        self.proximity: float = proximity

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.is_grayscale == self.is_grayscale) and
                (other.proximity == self.proximity))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.port, self.is_grayscale, self.proximity))

    @sense
    def colorname3(self) -> int:
        """
        Get the name of the detected color.

        Returns:
        enum value for the closest color detected
        out of ColorHue.RED, GREEN or BLUE (or NONE).
        """

    @sense
    def colorname12(self) -> int:
        """
        Get the name of the detected color.

        Returns:
        enum value of the closest color detected out of 12
        possible values of ColorType (or NONE).
        """

    @sense
    def grayscale(self, raw: bool = False) -> int:
        """
        Get the grayscale value detected by the color sensor.

        Parameters:
        - raw: if True, raw value will be returned, otherwise a percentage

        Returns:
        integer that represents the detected grayscale value
        (percentage 0-100 or raw 0-1024).
        """

    @sense
    def near(self) -> bool:
        """
        Check to see if an object is detected by the color sensor.

        Returns:
        True if an object has been detected, False otherwise
        """

    @act
    def set_proximity_threshold(self, proximity: float = 700):
        """
        Set the near threshold setting.

        Parameters:
        - proximity: threshold (higher is closer) (default 700)
        """
        self.proximity: float = proximity

    @act
    def led(self, state: bool):
        """
        Turn the led on the color sensor on or off.

        Parameters:
        - state: if True, LED will be turned on
        """
