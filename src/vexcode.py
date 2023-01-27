"""VEXcode VR."""


from collections.abc import Sequence
from typing import LiteralString

from vex import (
    Ports,
    Brain, BrainButton, BrainLcd, BrainSound, NoteType,
    Bumper,
    ColorHue, Colorsensor,
    Sonar,
    Controller, ControllerAxis, ControllerButton,
    Gyro, GyroCalibrationType,
    Motor,
    BrakeType, DirectionType, TorqueUnits, TurnType, VelocityUnits,
    FadeType, Touchled,
    TimeUnits, wait,
    DistanceUnits, RotationUnits,
    DEGREES, TURNS,
    PERCENT,
    SECONDS,
    INCHES, MM,
    FORWARD, REVERSE,
    LEFT, RIGHT,
)
from drivetrain import Drivetrain


__all__: Sequence[LiteralString] = (
    'Ports',
    'Brain', 'BrainButton', 'BrainLcd', 'BrainSound', 'NoteType',
    'Bumper',
    'ColorHue', 'Colorsensor',
    'Sonar',
    'Controller', 'ControllerAxis', 'ControllerButton',
    'Gyro', 'GyroCalibrationType',
    'Motor',
    'BrakeType', 'DirectionType', 'TorqueUnits', 'TurnType', 'VelocityUnits',
    'FadeType', 'Touchled',
    'TimeUnits', 'wait',
    'DistanceUnits', 'RotationUnits',
    'DEGREES', 'TURNS',
    'PERCENT',
    'SECONDS',
    'INCHES', 'MM',
    'FORWARD', 'REVERSE',
    'LEFT', 'RIGHT',
    'MSEC', 'SEC',
    'drivetrain',
    'vr_thread',
)


MSEC = TimeUnits.MSEC
SEC = SECONDS


drivetrain = Drivetrain(Motor(Ports.PORT1),
                        Motor(Ports.PORT6, True))


def vr_thread(*args):   # pylint: disable=unused-argument
    """VR Thread."""
