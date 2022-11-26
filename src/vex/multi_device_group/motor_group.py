"""2-Motor Group."""


from collections.abc import Sequence
from typing import Literal
from typing_extensions import Self

from abm.decor import act, sense

from ..motor import Motor
from ..motor.brake_type import BrakeType, BRAKE
from ..motor.current_units import CurrentUnits
from ..motor.direction_type import DirectionType, FORWARD
from ..motor.torque_units import TorqueUnits
from ..motor.velocity_units import VelocityUnits
from ..time.time_units import TimeUnits, SECONDS
from .._common_enums.numeric import NumType, PERCENT
from .._common_enums.rotation import RotationUnits, DEGREES


__all__: Sequence[str] = ('MotorGroup',)


class MotorGroup:
    """2-Motor Group."""

    def __init__(self, motor_a: Motor, motor_b: Motor, /):
        """Initialize 2-Motor Group."""
        self.motor_a: Motor = motor_a
        self.motor_b: Motor = motor_b

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, MotorGroup) and
                (other.motor_a == self.motor_a) and
                (other.motor_b == self.motor_b))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.motor_a, self.motor_b))

    @sense
    def current(self, units: Literal[CurrentUnits.AMP] = CurrentUnits.AMP) -> float:  # noqa: E501
        """Return electrical current."""

    @sense
    def is_done(self) -> bool:
        """Check whether both motors have finished spinning."""

    @sense
    def is_spinning(self) -> bool:
        """Check whether one or both of the motors is/are still spinning."""

    @sense
    def position(self, units: RotationUnits = DEGREES) -> float:
        """Return cumulative rotational angle."""

    @act
    def set_max_torque(self, value: NumType = 50, units: TorqueUnits = PERCENT):  # noqa: E501
        """Set max torque limit."""

    @act
    def set_position(self, value: NumType = 0, units: RotationUnits = DEGREES):
        """Set cumulative rotational position to specified angle."""

    @act
    def set_stopping(self, mode: BrakeType = BRAKE):
        """Set motor braking/stopping mode."""

    @act
    def set_timeout(self, time: NumType = 1, /, units: TimeUnits = SECONDS):
        """Set motor timeout."""

    @act
    def set_velocity(self, velocity: NumType = 50, units: VelocityUnits = PERCENT):  # noqa: E501
        """Set velocity."""

    @act
    def spin(self, direction: DirectionType = FORWARD):
        """Spin motors in specified direction."""

    @act
    def spin_for(self, direction: DirectionType = FORWARD,
                 rotation: NumType = 90, unit: RotationUnits = DEGREES,
                 wait: bool = True):
        """Spin motors in specified direction by specified angle."""

    @act
    def spin_to_position(self,
                         angle: NumType = 90, units: RotationUnits = DEGREES,
                         wait: bool = True):
        """Spin motors to specified rotational position."""

    @act
    def stop(self):
        """Stop motors."""

    @sense
    def velocity(self, units: VelocityUnits = PERCENT) -> float:
        """Return velocity."""
