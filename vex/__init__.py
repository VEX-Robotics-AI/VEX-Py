"""
VexIQ Python API B for Robot Mesh.
"""


# CLASSES
# =======


class Brain:
    """
    Use the Brain class to see battery information, or write to the screen.
    """

    def __init__(self):
        ...


class BrainButton:
    """
    Use the button class to get values from the brain's buttons.
    """
    ...


class BrainLcd:
    ...


class BrainSound:
    ...


class BrakeType:
    """
    The defined units for brake values.
    """
    ...


class Bumper:
    ...


class ColorHue:
    """
    Defined color hue values.
    """
    ...


class Colorsensor:
    ...


class Controller:
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


class Device:
    """
    Base class for all Vex IQ devices.
    """
    ...


class DirectionType:
    """
    The defined units for direction values.
    """
    ...


class DistanceUnits:
    """
    The measurement units for distance values.
    """
    ...


class Enum:
    ...


class FadeType:
    ...


class Gyro:
    ...


class GyroCalibrationType:
    ...


class Motor:
    ...


class NoteType:
    """
    Musical note to play.
    """
    ...


class Ports:
    ...


class RotationUnits:
    """
    The measurement units for rotation values.
    """
    ...


class Sonar:
    ...


class TimeUnits:
    """
    The measurement units for time values.
    """
    ...


class TorqueUnits:
    """
    The measurement units for torque values.
    """
    ...


class Touchled:
    """
    Use this class when programming with the touch LED device.
    """
    ...


class TurnType:
    """
    Left or right turn.
    """
    ...


class VelocityUnits:
    """
    The measurement units for velocity values.
    """
    ...


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
