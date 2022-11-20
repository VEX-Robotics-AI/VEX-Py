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
from ..units_common.distance import DistanceUnits
from ..units_common.electric import CurrentUnits
from ..units_common.rotation import RotationUnits
from ..util.doc import vexcode_doc

from .motor_group import MotorGroup


class DriveTrain(MotorGroup):
    """Drive Train."""


__all__: Sequence[str] = ('Drivetrain',)


