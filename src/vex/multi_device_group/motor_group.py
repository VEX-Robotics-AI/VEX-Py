"""Motor Group."""


from collections.abc import Sequence

from abm.decor import act, sense

from ..motor import Motor
from ..motor.brake_type import BrakeType
from ..motor.direction_type import DirectionType
from ..motor.velocity_units import VelocityUnits
from ..time.time_units import TimeUnits
from ..units_common.electric import ElectricCurrentUnits
from ..units_common.rotation import RotationUnits


__all__: Sequence[str] = ('MotorGroup',)


class MotorGroup:
    """Motor Group."""

    def __init__(self, motor_a: Motor, motor_b: Motor, /):
        """Initialize 2-Motor Group."""
        self.motor_a: Motor = motor_a
        self.motor_b: Motor = motor_b

    @sense
    def current(self, unit: ElectricCurrentUnits, /) -> float:
        """Return electric current."""

    @sense
    def is_done(self) -> bool:
        """Check whether motors have finished spinning."""

    @sense
    def is_spinning(self) -> bool:
        """Check whether some of the motors are still spinning."""

    @sense
    def position(self, unit: RotationUnits, /) -> float:
        """Return rotational position."""

    @act
    def set_max_torque(self, unit, /):
        """Set max torque limit."""

    @act
    def set_position(self, position: float, unit: RotationUnits, /):
        """Set rotational position to specified value."""

    @act
    def set_stopping(self, mode: BrakeType, /):
        """Set motor braking/stopping mode."""

    @act
    def set_timeout(self, value: float, unit: TimeUnits, /):
        """Set motor timeout."""

    @act
    def set_velocity(self, velocity: float, unit: VelocityUnits, /):
        """Set velocity."""

    @act
    def spin(self, direction: DirectionType, /):
        """Spin motors in specified direction."""

    @act
    def spin_for(self,
                 direction: DirectionType,
                 angle: float, unit: RotationUnits,
                 wait: bool = True):
        """Spin motors in specified direction by specified angle."""

    @act
    def spin_to_position(self, angle: float, unit: RotationUnits, wait: bool = True):  # noqa: E501
        """Spin motors to specified rotational position."""
