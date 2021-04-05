"""
VexIQ Python API B for Robot Mesh.
"""


from __future__ import annotations
from typing import Any


# CLASSES
# =======


class Device:
    """
    Base class for all Vex IQ devices.
    """
    ...


class Enum:
    ...


class Brain:
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
        self.id = id

    def pressing(self) -> bool:
        """
        Gets the pressed status of a button.

        Returns
        True if pressed, False othewise.
        """
        ...


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
        ...

    def clear_screen(self):
        """
        Clears the whole screen.
        """
        ...


class BrainSound:
    ...


class BrakeType(Enum):
    """
    The defined units for brake values.
    """
    COAST: int = 0   # A brake unit that is defined as coast.
    BRAKE: int = 1   # A brake unit that is defined as brake.
    HOLD: int = 2   # A brake unit that is defined as hold.


class Bumper:
    ...


class ColorHue(Enum):
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


class Colorsensor:
    ...


class Controller:
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """
    ...


class ControllerAxis:
    """
    Use the axis class to get values from one of the controller's joysticks.
    """
    ...


class ControllerButton:
    """
    Use the button class to get values from the controller's buttons.
    """
    ...


class DirectionType(Enum):
    """
    The defined units for direction values.
    """
    FWD: int = 0   # A direction unit that is defined as forward.
    REV: int = 1   # A direction unit that is defined as backward.


class DistanceUnits:
    """
    The measurement units for distance values.
    """
    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.


class FadeType:
    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2


class Gyro:
    ...


class GyroCalibrationType(Enum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2


class Motor:
    ...


class NoteType:
    """
    Musical note to play.
    """
    ...


class Ports:
    ...


class RotationUnits:
    """
    The measurement units for rotation values.
    """
    ...


class Sonar:
    ...


class TimeUnits:
    """
    The measurement units for time values.
    """
    ...


class TorqueUnits:
    """
    The measurement units for torque values.
    """
    ...


class Touchled:
    """
    Use this class when programming with the touch LED device.
    """
    ...


class TurnType:
    """
    Left or right turn.
    """
    ...


class VelocityUnits:
    """
    The measurement units for velocity values.
    """
    ...


# FUNCTIONS
# =========


def wait(time: float, timeUnits: TimeUnits = TimeUnits.SEC):
    """
    Wait for a specific amount of time.
    Identical to sys.sleep().

    Parameters
    time: The length of time to wait
    timeUnits: The units of time (default seconds)
    """
    ...


# CONSTANTS/VARIABLES
# ===================


INT29_MAX: int = 0x1FFFFFFF

DEGREES: RotationUnits = RotationUnits.DEG
TURNS: RotationUnits = RotationUnits.REV

PERCENT: VelocityUnits = VelocityUnits.PCT

SECONDS: TimeUnits = TimeUnits.SEC

INCHES: DistanceUnits = DistanceUnits.IN
MM: DistanceUnits = DistanceUnits.MM

FORWARD: DirectionType = DirectionType.FWD
REVERSE: DirectionType = DirectionType.REV

LEFT: TurnType = TurnType.LEFT
RIGHT: TurnType = TurnType.RIGHT
