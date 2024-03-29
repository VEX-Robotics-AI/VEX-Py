"""VEX module.

VEXcode IQ: codeiq.vex.com
VEXcode V5: codev5.vex.com
VEXcode VR: vr.vex.com

Robot Mesh VEX IQ Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/namespacevex.html
"""


from collections.abc import Callable, Sequence
from importlib.metadata import version
import string
import sys
from threading import Thread
from typing import LiteralString, Optional

from abm import interactive

from ._device import Device, TriDevice, V5DeviceType

from .brain import (
    Brain, BrainBattery, BrainButton,
    BrainLcd,
    Font,
    MONO_M, MONO_L, MONO_XL, MONO_XXL, MONO_S, MONO_XS,
    PROP_M, PROP_L, PROP_XL, PROP_XXL,
    FontType,
    BrainSound, NoteType, SoundType)

from .brain.port import Ports

from .controller import (Controller,
                         ControllerAxis,
                         ControllerButton,
                         ControllerType, PRIMARY, PARTNER)

from .brain.inertial_sensor import Inertial

from .motor import (Motor,
                    BrakeType, COAST, BRAKE, HOLD,
                    CurrentUnits,
                    DirectionType, FORWARD, REVERSE,
                    GearSetting,
                    TurnType, LEFT, RIGHT,
                    TorqueUnits,
                    VoltageUnits)

from .bumper_switch_sensor import Bumper
from .color_sensor import ColorSensor, Colorsensor
from .distance_sensor import Distance, ObjectSizeType, Sonar
from .gyro_sensor import Gyro, GyroCalibrationType
from .optical_sensor import Optical, LedStateType, GestureType
from .touch_led import Touchled, FadeType
from .vision_sensor import Vision, VisionObject

from .multi_device_group import MotorGroup, DriveTrain, SmartDrive

from .time import Timer, TimeUnits, SECONDS, MSEC, clock, wait

from ._common_enums import (AnalogUnits,
                            AxisType, XAXIS, YAXIS, ZAXIS,
                            Color, ColorHue,
                            DistanceUnits, MM, INCHES,
                            OrientationType, ROLL, PITCH, YAW,
                            PercentUnits, PERCENT,
                            PowerUnits,
                            RotationUnits, DEGREES, TURNS,
                            TemperatureUnits,
                            VelocityUnits, RPM, DPS)

from ._util.doc import robotmesh_doc
from ._util.type import Num


__all__: Sequence[LiteralString] = (
    '__version__',

    'Device', 'TriDevice', 'V5DeviceType',

    'Brain', 'BrainBattery', 'BrainButton',
    'BrainLcd',
    'Font',
    'MONO_M', 'MONO_L', 'MONO_XL', 'MONO_XXL', 'MONO_S', 'MONO_XS',
    'PROP_M', 'PROP_L', 'PROP_XL', 'PROP_XXL',
    'FontType',
    'BrainSound', 'NoteType', 'SoundType',

    'Ports',

    'Controller',
    'ControllerAxis',
    'ControllerButton',
    'ControllerType', 'PRIMARY', 'PARTNER',

    'Inertial',

    'Motor',
    'BrakeType', 'COAST', 'BRAKE', 'HOLD',
    'CurrentUnits',
    'DirectionType', 'FORWARD', 'REVERSE',
    'GearSetting',
    'TorqueUnits',
    'TurnType', 'LEFT', 'RIGHT',
    'VoltageUnits',

    'Bumper',
    'ColorSensor', 'Colorsensor',
    'Optical', 'LedStateType', 'GestureType',
    'Distance', 'ObjectSizeType',
    'Sonar',
    'Gyro', 'GyroCalibrationType',
    'Touchled', 'FadeType',
    'Vision', 'VisionObject',

    'MotorGroup', 'DriveTrain', 'SmartDrive',

    'Timer', 'TimeUnits', 'SECONDS', 'MSEC', 'wait',

    'AnalogUnits',
    'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
    'Color', 'ColorHue',
    'DistanceUnits', 'MM', 'INCHES',
    'OrientationType', 'ROLL', 'PITCH', 'YAW',
    'PercentUnits', 'PERCENT',
    'PowerUnits',
    'RotationUnits', 'DEGREES', 'TURNS',
    'TemperatureUnits',
    'VelocityUnits', 'RPM', 'DPS',

    'SYSTEM_DISPLAY_WIDTH', 'SYSTEM_DISPLAY_HEIGHT', 'STATUS_BAR_HEIGHT',
    'RUMBLE_LONG', 'RUMBLE_SHORT', 'RUMBLE_PULSE',

    'staticmethod',

    'interactive',
)


__version__: LiteralString = version(distribution_name='VEX-Py')


# CONSTANTS
# =========

INT29_MAX: int = 0x1FFFFFFF


SYSTEM_DISPLAY_WIDTH: int = 480
SYSTEM_DISPLAY_HEIGHT: int = 272
STATUS_BAR_HEIGHT: int = 32

RUMBLE_LONG: LiteralString = '----'
RUMBLE_SHORT: LiteralString = '....'
RUMBLE_PULSE: LiteralString = '-.-.'


# FUNCTIONS
# =========

@robotmesh_doc("""
    Runs the given function in a thread sharing the current global namespace.
""")
def run_in_thread(f: Callable, /):  # pylint: disable=invalid-name
    """Run specified function in parallel thread."""
    Thread(group=None, target=f, name=None, args=(), kwargs={}, daemon=True).start()  # noqa: E501


@robotmesh_doc("""
    Wait until a function returns a value.

    Returns True when reached, False on timeout.

    Parameters
    - func: function to run until it returns the value
    - value: return value to wait for; default True
    - timeout: timeout in seconds; if reached returns False;
               default None (no timeout)
    - check_period: time to wait between checks, in seconds;
                    default 0 (no wait)
""")
def wait_for(func: Callable, value: bool = True,
             timeout: Optional[int] = None, check_period: Num = 0, /) -> bool:
    # pylint: disable=unused-argument
    """Wait for specified function to return specified target value."""


# ALIASES
# =======


# STRING module
# Robot Mesh VEX IQ Python B:
# robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacestring.html
# Robot Mesh VEX V5 Python:
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacestring.html
# --------------------------------------------------------------------------

string.letters: LiteralString = string.ascii_letters


# SYS module
# Robot Mesh VEX IQ Python B:
# robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacesys.html
# Robot Mesh VEX V5 Python:
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacesys.html
# -----------------------------------------------------------------------

sys.clock: Callable[[], Num] = clock
sys.sleep: Callable[[Num, TimeUnits], None] = wait
sys.maxint: int = INT29_MAX
sys.run_in_thread: Callable[[Callable], None] = run_in_thread
sys.wait_for: Callable[[Callable, bool, Optional[int], Num], None] = wait_for


# misc/other
# ----------

# pylint: disable=redefined-builtin
staticmethod: Callable[[Callable], Callable] = staticmethod
