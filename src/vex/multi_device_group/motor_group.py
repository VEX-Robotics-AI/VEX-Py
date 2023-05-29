"""2-Motor Group."""


from collections.abc import Sequence
from typing import Literal, LiteralString, Self

from abm.decor import act, sense

from ..motor import Motor
from ..motor.brake import BrakeType, BRAKE
from ..motor.current import CurrentUnits
from ..motor.direction import DirectionType, FORWARD
from ..motor.torque import TorqueUnits
from ..time.units import TimeUnits, SECONDS
from .._common_enums.percent import PERCENT
from .._common_enums.rotation import RotationUnits, DEGREES
from .._common_enums.velocity import VelocityUnits

from .._util.type import Num


__all__: Sequence[LiteralString] = ('MotorGroup',)


class MotorGroup:
    """2-Motor Group."""

    def __init__(self: Self, motor_a: Motor, motor_b: Motor, /):
        """Initialize 2-Motor Group."""
        self.motor_a: Motor = motor_a
        self.motor_b: Motor = motor_b

    def __eq__(self: Self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, MotorGroup) and
                (other.motor_a == self.motor_a) and
                (other.motor_b == self.motor_b))

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        return hash((self.motor_a, self.motor_b))

    @sense
    def current(self: Self,
                units: Literal[CurrentUnits.AMP] = CurrentUnits.AMP) -> float:
        """Return electrical current."""

    @sense
    def is_done(self: Self) -> bool:
        """Check whether both motors have finished spinning."""

    @sense
    def is_spinning(self: Self) -> bool:
        """Check whether one or both of the motors is/are still spinning."""

    @sense
    def position(self: Self, units: RotationUnits = DEGREES) -> float:
        """Return rotational angle."""

    @act
    def set_max_torque(self: Self, value: Num = 50, units: TorqueUnits = PERCENT):  # noqa: E501
        """Set max torque limit."""

    @act
    def set_position(self: Self, value: Num = 0, units: RotationUnits = DEGREES):  # noqa: E501
        """Set rotational position to specified angle."""

    @act
    def set_stopping(self: Self, mode: BrakeType = BRAKE):
        """Set motor braking/stopping mode."""

    @act
    def set_timeout(self: Self, time: Num = 1, /, units: TimeUnits = SECONDS):  # noqa: E501
        """Set motor timeout."""

    @act
    def set_velocity(self: Self,
                     velocity: Num = 50, units: VelocityUnits = PERCENT):
        """Set velocity."""

    @act
    def spin(self: Self, direction: DirectionType = FORWARD):
        """Spin motors in specified direction."""

    @act
    def spin_for(self: Self, direction: DirectionType = FORWARD,
                 rotation: Num = 90, unit: RotationUnits = DEGREES,
                 wait: bool = True):
        """Spin motors in specified direction by specified angle."""

    @act
    def spin_to_position(self: Self,
                         angle: Num = 90, units: RotationUnits = DEGREES,
                         wait: bool = True):
        """Spin motors to specified rotational position."""

    @act
    def stop(self: Self):
        """Stop motors."""

    @sense
    def velocity(self: Self, units: VelocityUnits = PERCENT) -> float:
        """Return velocity."""
