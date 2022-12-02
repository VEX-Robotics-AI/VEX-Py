"""VEX module.

VEXcode IQ: codeiq.vex.com
VEXcode V5: codev5.vex.com
VEXcode VR: vr.vex.com

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html
"""


from collections.abc import Sequence
from importlib.metadata import version
import sys
from typing import Optional

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
                            NumType, PERCENT,
                            DistanceUnits, MM, INCHES,
                            RotationUnits, DEGREES, TURNS)

from ._util.doc import robotmesh_doc


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


# FUNCTIONS
# =========
@robotmesh_doc("""
    Wait until a function returns a value.

    Returns True when reached, False on timeout.

    Parameters:
    - func: function to run until it returns the value
    - value: return value to wait for; default True
    - timeout: timeout in seconds; if reached returns False;
               default None (no timeout)
    - check_period: time to wait between checks, in seconds;
                    default 0 (no wait)
""")
def wait_for(func: callable,
             value: bool = True,
             timeout: Optional[int] = None,
             check_period: NumType = 0) -> bool:
    # pylint: disable=unused-argument
    """Wait for specified function to return specified target value."""


# ALIASES
# =======
sys.sleep: callable = wait
sys.maxint: int = INT29_MAX
sys.wait_for: callable = wait_for
