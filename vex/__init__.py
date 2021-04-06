"""
VexIQ Python API B for Robot Mesh.
"""


from __future__ import annotations


# CLASSES
# =======
from .abstract import Device, Enum
from .port import Ports
from .brain import Brain, BrainButton, BrainLcd, BrainSound, NoteType
from .bumper_switch_sensor import Bumper
from .color_sensor import ColorHue, Colorsensor
from .distance_sensor import Sonar
from .controller import Controller, ControllerAxis, ControllerButton
from .gyro_sensor import Gyro, GyroCalibrationType
from .motor import (
    BrakeType, DirectionType, Motor, TorqueUnits, TurnType, VelocityUnits
)
from .touch_led import FadeType, Touchled
from .time import TimeUnits, wait


class DistanceUnits(Enum):
    """
    The measurement units for distance values.
    """
    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.


class RotationUnits(Enum):
    """
    The measurement units for rotation values.
    """
    DEG: int = 0   # A rotation unit that is measured in degrees.
    REV: int = 1   # A rotation unit that is measured in revolutions.
    RAW: int = 99   # A rotation unit that is measured in raw data form.


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
