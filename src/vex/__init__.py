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
)
from .brain.port import Ports
from .bumper_switch_sensor import Bumper
from .color_sensor import ColorSensor, Colorsensor, ColorHue
from .distance_sensor import Sonar
from .controller import Controller, ControllerAxis, ControllerButton
from .inertial import Inertial, AxisType, OrientationType
from .gyro_sensor import Gyro, GyroCalibrationType
from .motor import (Motor,
                    BrakeType,
                    DirectionType, FORWARD, REVERSE,
                    TurnType, LEFT, RIGHT,
                    TorqueUnits,
                    VelocityUnits, PERCENT)
from .touch_led import Touchled, FadeType
from .time import TimeUnits, SECONDS, MSEC, wait
from .units_common import (DistanceUnits, MM, INCHES, CM,
                           RotationUnits, DEGREES, TURNS,
                           CurrentUnits, AMP)


__all__: Sequence[str] = (
    '__version__',
    'Brain', 'BrainButton', 'BrainLcd', 'BrainSound', 'NoteType', 'SoundType',
    'Ports',
    'Inertial',
    'AxisType',
    'OrientationType',
    'Bumper',
    'ColorSensor', 'Colorsensor', 'ColorHue',
    'Sonar',
    'Controller', 'ControllerAxis', 'ControllerButton',
    'Gyro', 'GyroCalibrationType',
    'Motor',
    'BrakeType',
    'DirectionType', 'FORWARD', 'REVERSE',
    'TorqueUnits',
    'TurnType', 'LEFT', 'RIGHT',
    'VelocityUnits', 'PERCENT',
    'Touchled', 'FadeType',
    'TimeUnits', 'SECONDS', 'MSEC', 'wait',
    'DistanceUnits', 'MM', 'INCHES', 'CM',
    'RotationUnits', 'DEGREES', 'TURNS',
    'CurrentUnits', 'AMP',
    'interactive',
)


__version__: str = version(distribution_name="VEX-Py")


# CONSTANTS
# =========
INT29_MAX: int = 0x1FFFFFFF


# ALIASES
# =======
sys.sleep: callable = wait
