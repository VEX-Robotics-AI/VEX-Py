"""
VexIQ Python API B for Robot Mesh.
"""


from __future__ import annotations


# CLASSES
# =======
from .abstract import Device, Enum
from .port import Ports
from .brain import Brain, BrainButton, BrainLcd, BrainSound
from .bumper_switch_sensor import Bumper
from .color_sensor import ColorHue, Colorsensor
from .controller import Controller, ControllerAxis, ControllerButton
from .motor import BrakeType, DirectionType, Motor
from .touch_led import FadeType, Touchled


class DistanceUnits(Enum):
    """
    The measurement units for distance values.
    """
    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.



class Gyro(Device):
    ...


class GyroCalibrationType(Enum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2


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
