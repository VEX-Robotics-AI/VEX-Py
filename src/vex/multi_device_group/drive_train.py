"""Drive Train."""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self

from abm.decor import act, sense

from ..motor import Motor
from ..motor.brake_type import BrakeType
from ..motor.direction_type import DirectionType, FORWARD
from ..motor.turn_type import TurnType
from ..motor.velocity_units import VelocityUnits
from ..time.time_units import TimeUnits
from ..units_common.distance import DistanceUnits, MM
from ..units_common.electric import CurrentUnits
from ..units_common.rotation import RotationUnits
from ..util.doc import vexcode_doc

from .motor_group import MotorGroup


__all__: Sequence[str] = ('DriveTrain',)


class DriveTrain(MotorGroup):
    """Drive Train."""

    def __init__(  # pylint: disable=super-init-not-called
            self,
            left_motor: Motor, right_motor: Motor,
            wheel_base: float = 200, track_width: float = 176,
            length_unit: DistanceUnits = MM,
            gear_ratio: float = 1, /):
        """Initialize Drivetrain."""
        self.left_motor: Motor = left_motor
        self.right_motor: Motor = right_motor
        self.wheel_base: float = wheel_base
        self.track_width: float = track_width
        self.length_unit: DistanceUnits = length_unit
        self.gear_ratio: float = gear_ratio


    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return (isinstance(other, DriveTrain) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.wheel_base == self.wheel_base) and
                (other.track_width == self.track_width) and
                (other.length_unit == self.length_unit) and
                (other.gear_ratio == self.gear_ratio))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.left_motor, self.right_motor,
                     self.wheel_base, self.track_width,
                     self.length_unit, self.gear_ratio))

