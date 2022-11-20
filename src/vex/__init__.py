"""VEX module.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html
"""


from collections.abc import Sequence
from importlib.metadata import version
import sys

from abm import interactive

from ._abstract_device import Device
from .brain import (
    Brain,
    BrainButton,
    BrainLcd,
    BrainSound,
    NoteType,
    SoundType,
)
from .brain.port import Ports
from .brain.inertial_sensor import Inertial, AxisType, OrientationType
from .bumper_switch_sensor import Bumper
from .color_sensor import ColorSensor, Colorsensor, ColorHue
from .distance_sensor import Distance, ObjectSizeType, Sonar
from .controller import Controller, ControllerAxis, ControllerButton
from .gyro_sensor import Gyro, GyroCalibrationType
from .motor import (Motor,
                    BrakeType, COAST, BRAKE, HOLD,
                    CurrentUnits,
                    DirectionType, FORWARD, REVERSE,
                    TurnType, LEFT, RIGHT,
                    TorqueUnits,
                    VelocityUnits, RPM, DPS)
from .optical_sensor import Optical, LedStateType, GestureType
from .touch_led import Touchled, FadeType
from .time import TimeUnits, SECONDS, MSEC, wait
from .units_common import (PERCENT,
                           DistanceUnits, MM, INCHES,
                           RotationUnits, DEGREES, TURNS)


__all__: Sequence[str] = (
    '__version__',
    'Device',
    'Brain', 'BrainButton', 'BrainLcd', 'BrainSound', 'NoteType', 'SoundType',
    'Ports',
    'Controller', 'ControllerAxis', 'ControllerButton',
    'Inertial',
    'AxisType',
    'OrientationType',
    'Motor',
    'BrakeType', 'COAST', 'BRAKE', 'HOLD',
    'CurrentUnits',
    'DirectionType', 'FORWARD', 'REVERSE',
    'TorqueUnits',
    'TurnType', 'LEFT', 'RIGHT',
    'VelocityUnits', 'RPM', 'DPS',
    'Bumper',
    'ColorSensor', 'Colorsensor', 'ColorHue',
    'Optical', 'LedStateType', 'GestureType',
    'Distance', 'ObjectSizeType',
    'Sonar',
    'Gyro', 'GyroCalibrationType',
    'Touchled', 'FadeType',
    'TimeUnits', 'SECONDS', 'MSEC', 'wait',
    'PERCENT',
    'DistanceUnits', 'MM', 'INCHES',
    'RotationUnits', 'DEGREES', 'TURNS',
    'interactive',
)


__version__: str = version(distribution_name='VEX-Py')


# CONSTANTS
# =========
INT29_MAX: int = 0x1FFFFFFF


# ALIASES
# =======
sys.sleep: callable = wait
sys.maxint: int = INT29_MAX
