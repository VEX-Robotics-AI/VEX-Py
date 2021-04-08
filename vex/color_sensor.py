from enum import IntEnum

from __decor import act, sense

from .abstract import Device


class ColorHue(IntEnum):
    """
    Defined color hue values.
    """
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
    """Color Sensor"""
    def __init__(self, index, is_grayscale=False, proximity=700):
        """
        Creates a new color sensor object on the port specified in the parameter.

        :params:
        index: The port index (zero-based)
        is_grayscale: Whether grayscale mode (LED on), default false
        proximity: threshold (default 700)
        """

    def colorname3(self):
        """
        Gets the name of the detected color.

        return:
        enum value for the closest color detected out of ColorHue.RED, GREEN or BLUE (or NONE).
        """

    def colorname12(self):
        """
        Gets the name of the detected color.

        return:
        enum value of the closest color detected out of 12 possible values of ColorType (or NONE).
        """

    def grayscale(self, raw=False):
        """
        Gets the grayscale value detected by the color sensor.

        params:
        raw: if True, raw value will be returned, otherwise a percentage

        return:
        integer that represents the detected grayscale value (percentage 0-100 or raw 0-1024).
        """

    def near(self):
        """
        Check to see if an object is detected by the color sensor.

        return:
        True if an object has been detected, False otherwise
        """

    def set_proximity_threshold(self, proximity):
        """
        Set the near threshold setting.

        params:
        proximity: threshold (higher is closer) (default 700)
        """


    def led(self, state):
        """
        Turns the led on the color sensor on or off.

        params:
        state: if True, LED will be turned on
        """
