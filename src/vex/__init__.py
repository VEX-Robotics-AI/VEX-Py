"""VEX module.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html
"""


from collections.abc import Sequence
from importlib.metadata import version
import sys

from abm import interactive

from .brain import (
    Brain,
    BrainButton,
    BrainLcd,
    BrainSound,
    NoteType,
    SoundType,
)  # noqa: E501
from .brain.port import Ports
from .bumper_switch_sensor import Bumper
from .color_sensor import Colorsensor, ColorHue
from .distance_sensor import Sonar
from .controller import Controller, ControllerAxis, ControllerButton
from .inertial import Inertial, AxisType, OrientationType
from .gyro_sensor import Gyro, GyroCalibrationType
from .motor import Motor, BrakeType, DirectionType, TurnType, TorqueUnits, VelocityUnits
from .touch_led import Touchled, FadeType
from .time import TimeUnits, wait
from .units_common import DistanceUnits, RotationUnits


__all__: Sequence[str] = (
    "__version__",
    "Brain",
    "BrainButton",
    "BrainLcd",
    "BrainSound",
    "NoteType",
    "SoundType",
    "Ports",
    "Bumper",
    "Colorsensor",
    "ColorHue",
    "Inertial",
    "AxisType",
    "XAXIS",
    "YAXIS",
    "ZAXIS",
    "OrientationType",
    "PITCH",
    "ROLL",
    "YAW",
    "Sonar",
    "Controller",
    "ControllerAxis",
    "ControllerButton",
    "Gyro",
    "GyroCalibrationType",
    "Motor",
    "BrakeType",
    "DirectionType",
    "TorqueUnits",
    "TurnType",
    "VelocityUnits",  # noqa: E501
    "Touchled",
    "FadeType",
    "TimeUnits",
    "wait",
    "DistanceUnits",
    "RotationUnits",
    "DEGREES",
    "TURNS",
    "PERCENT",
    "SECONDS",
    "INCHES",
    "MM",
    "FORWARD",
    "REVERSE",
    "LEFT",
    "RIGHT",
    "interactive",
)


__version__: str = version(distribution_name="VEX-Py")


# CONSTANTS
# =========
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

XAXIS: AxisType = AxisType.XAXIS
YAXIS: AxisType = AxisType.YAXIS
ZAXIS: AxisType = AxisType.ZAXIS

PITCH: OrientationType = OrientationType.PITCH
ROLL: OrientationType = OrientationType.ROLL
YAW: OrientationType = OrientationType.YAW


# ALIASES
# =======
sys.sleep: callable = wait
