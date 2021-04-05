"""
VexIQ Python API B for Robot Mesh.
"""


from __future__ import annotations
from enum import IntEnum
from typing import Any


# CLASSES
# =======


class Device:
    """
    Base class for all Vex IQ devices.
    """
    ...


class Enum(IntEnum):
    ...


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


class Bumper(Device):
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


class Colorsensor(Device):
    ...


class Controller(Device):
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


class DistanceUnits(Enum):
    """
    The measurement units for distance values.
    """
    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.


class FadeType(Enum):
    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2


class Gyro(Device):
    ...


class GyroCalibrationType(Enum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2


class Motor(Device):
    ...


class NoteType(Enum):
    """
    Musical note to play.
    """
    silence: int = 0   # Stop playing/play a silence.
    C: int = 1
    D: int = 2
    E: int = 3
    F: int = 4
    G: int = 5
    A: int = 6
    B: int = 7


class Ports(Enum):
    PORT1: int = 0
    PORT2: int = 1
    PORT3: int = 2
    PORT4: int = 3
    PORT5: int = 4
    PORT6: int = 5
    PORT7: int = 6
    PORT8: int = 7
    PORT9: int = 8
    PORT10: int = 9
    PORT11: int = 10
    PORT12: int = 11


class RotationUnits(Enum):
    """
    The measurement units for rotation values.
    """
    DEG: int = 0   # A rotation unit that is measured in degrees.
    REV: int = 1   # A rotation unit that is measured in revolutions.
    RAW: int = 99   # A rotation unit that is measured in raw data form.


class Sonar(Device):
    ...


class TimeUnits(Enum):
    """
    The measurement units for time values.
    """
    SEC: int = 0   # A time unit that is measured in seconds.
    MSEC: int = 1   # A time unit that is measured in milliseconds.


class TorqueUnits(Enum):
    """
    The measurement units for torque values.
    """
    NM: int = 0   # A torque unit that is measured in Newton Meters.
    IN_LB: int = 1   # A torque unit that is measured in Inch Pounds.


class Touchled(Device):
    """
    Use this class when programming with the touch LED device.
    """
    ...


class TurnType(Enum):
    """
    Left or right turn.
    """
    LEFT: int = 0
    RIGHT: int = 1


class VelocityUnits(Enum):
    """
    The measurement units for velocity values.
    """
    PCT: int = 0   # A velocity unit that is measured in percentage.
    RPM: int = 1   # A velocity unit that is measured in rotations per minute.
    DPS: int = 2   # A velocity unit that is measured in degrees per second.
    RAW: int = 99   # A velocity unit that is measured in raw data form.


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
