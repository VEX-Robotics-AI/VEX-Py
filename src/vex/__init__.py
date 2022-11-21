"""VEX module.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html
"""


from collections.abc import Sequence
from importlib.metadata import version
import sys

from abm import interactive

# from ._abstract_device import Device

from .brain import (Brain, BrainButton,
                    BrainLcd, FontType,
                    BrainSound, NoteType, SoundType)

from .brain.port import Ports

from .controller import Controller, ControllerAxis, ControllerButton

from .brain.inertial_sensor import (Inertial,
                                    AxisType, XAXIS, YAXIS, ZAXIS,
                                    OrientationType, PITCH, ROLL, YAW)

from .motor import (Motor,
                    BrakeType, COAST, BRAKE, HOLD,
                    CurrentUnits,
                    DirectionType, FORWARD, REVERSE,
                    TurnType, LEFT, RIGHT,
                    TorqueUnits,
                    VelocityUnits, RPM, DPS)

from .bumper_switch_sensor import Bumper
from .color_sensor import ColorSensor, Colorsensor
from .distance_sensor import Distance, ObjectSizeType, Sonar
from .gyro_sensor import Gyro, GyroCalibrationType
from .optical_sensor import Optical, LedStateType, GestureType
from .touch_led import Touchled, FadeType

from .multi_device_group import MotorGroup, DriveTrain, SmartDrive

from .time import TimeUnits, SECONDS, MSEC, wait

from ._common_enums import (Color, ColorHue,
                            PERCENT,
                            DistanceUnits, MM, INCHES,
                            RotationUnits, DEGREES, TURNS)


__all__: Sequence[str] = (
    '__version__',

    # 'Device',

    'Brain', 'BrainButton',
    'BrainLcd', 'FontType',
    'BrainSound', 'NoteType', 'SoundType',

    'Ports',

    'Controller', 'ControllerAxis', 'ControllerButton',

    'Inertial',
    'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
    'OrientationType', 'PITCH', 'ROLL', 'YAW',

    'Motor',
    'BrakeType', 'COAST', 'BRAKE', 'HOLD',
    'CurrentUnits',
    'DirectionType', 'FORWARD', 'REVERSE',
    'TorqueUnits',
    'TurnType', 'LEFT', 'RIGHT',
    'VelocityUnits', 'RPM', 'DPS',

    'Bumper',
    'ColorSensor', 'Colorsensor',
    'Optical', 'LedStateType', 'GestureType',
    'Distance', 'ObjectSizeType',
    'Sonar',
    'Gyro', 'GyroCalibrationType',
    'Touchled', 'FadeType',

    'MotorGroup', 'DriveTrain', 'SmartDrive',

    'TimeUnits', 'SECONDS', 'MSEC', 'wait',

    'Color', 'ColorHue',
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
