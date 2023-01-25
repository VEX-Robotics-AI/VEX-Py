"""VEX Motor Group.

Robot Mesh VEX IQ Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacemotor__group.html

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/namespacemotor__group.html
"""


from collections.abc import Sequence
from typing import Optional, Self

from abm.decor import act, sense

from vex.motor import Motor
from vex.motor.brake_type import BrakeType
from vex.motor.direction_type import DirectionType
from vex.motor.torque_units import TorqueUnits
from vex.motor.velocity_units import VelocityUnits
from vex.time.time_units import TimeUnits
from vex._common_enums.rotation import RotationUnits

from vex._util.doc import robotmesh_doc
from vex._util.type import NumType


__all__: Sequence[str] = ('MotorGroup',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classmotor__group_1_1_motor_group.html
""")
class MotorGroup:  # pylint: disable=too-many-public-methods
    """Motor Group."""

    @robotmesh_doc("""
        Create a new motor group with specified motors.

        param:
        - motors: a list or tuple of motors in the group
    """)
    def __init__(self, motors: list[Motor], /):
        """Initialize Motor Group."""
        self.motors: list[Motor] = motors
        self.rotations: dict[Motor, dict[RotationUnits, NumType]] = \
            {motor: {} for motor in motors}

        self.velocities: dict[VelocityUnits, NumType] = \
            dict[VelocityUnits, NumType]()
        self.stopping: Optional[BrakeType] = None
        self.timeouts: dict[TimeUnits, NumType] = dict[TimeUnits, NumType]()
        self.max_torque: dict[TorqueUnits, NumType] = dict[TorqueUnits, NumType]()  # noqa: E501

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, MotorGroup) and \
            (set(other.motors) == set(self.motors))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash(set(self.motors))

    @robotmesh_doc("""
        Return the number of motors in the motor group.

        Returns:
        number of motors
    """)
    def count(self) -> int:
        """Count number of motors."""
        return len(self.motors)

    @robotmesh_doc("""
        Set velocity of motor group based on parameters set in command.

        This command will not run the motor.
        Any subsequent call that does not contain a specified motor velocity
        will use this value.

        Parameters
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for velocity,
                         a VelocityUnits enum value.
    """)
    @act
    def set_velocity(self, velocity: NumType, velocityUnits=VelocityUnits.PCT, /):  # noqa: E501
        """Set motor velocity."""
        self.velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters
        - brakeType: The stopping mode can be set
                     to BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def set_stopping(self, brakeType: BrakeType, /):
        """Set motor stopping mode."""
        self.stopping: BrakeType = brakeType

    @robotmesh_doc("""
        Reset all motor encoders to the value of zero.
    """)
    @act
    def reset_rotation(self):
        """Reset motors' rotational angle to 0."""
        for motor in self.motors:
            for rotation_unit in self.rotations[motor]:
                self.rotations[motor][rotation_unit] = 0

    @robotmesh_doc("""
        Set value of all motor encoders to value specified in parameter.

        Parameters
        - value: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation,
                         a RotationUnits enum value.
    """)
    @act
    def set_rotation(self, value: NumType, rotationUnits=RotationUnits.DEG, /):
        """Set motors' rotational angle to specified value."""
        for motor in self.motors:
            self.rotations[motor][rotationUnits] = value

    @robotmesh_doc("""
        Set the timeout for the motor group.

        If the motor group does not reach its commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
    """)
    @act
    def set_timeout(self, time: NumType, timeUnits=TimeUnits.SEC, /):
        """Set motor timeout."""
        self.timeouts[timeUnits] = time

    @robotmesh_doc("""
        Return a timeout in given time units.
    """)
    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC, /) -> NumType:
        """Return motor timeout."""
        return self.timeouts[timeUnits]

    @robotmesh_doc("""
        Return True if the last motor operation on any motor timed out.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Check whether motors timed out."""

    @robotmesh_doc("""
        Turn on the motors and spins them.

        (in the specified direction and a specified velocity)

        Parameters
        - dir: The direction to spin the motors,
               a DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
    """)
    @act
    def spin(self, dir: DirectionType,  # pylint: disable=redefined-builtin
             velocity: Optional[NumType] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin motors."""

    @robotmesh_doc("""
        Turn on the motors and spin them.

        (to an absolute target rotation value at a specified velocity)

        Returns:
        Returns a Boolean that signifies when
        the motors have reached the target rotation value.

        Parameters
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion (Optional): If True, your program will wait
                                        until the motor reaches the target
                                        rotational value.
                                        If false, the program will continue
                                        after calling this function.
                                        By default, this parameter is true.
    """)
    @act
    def spin_to(self,
                rotation: NumType, rotationUnits: RotationUnits = RotationUnits.DEG,  # noqa: E501
                velocity: Optional[NumType] = None,
                velocityUnits: VelocityUnits = VelocityUnits.PCT,
                waitForCompletion: bool = True, /) -> bool:
        """Spin motors to specified target rotational angle."""

    @robotmesh_doc("""
        Turn on the motors and spin them.

        (to a relative target rotation value at a specified velocity)

        Returns:
        True if motors have reached the target rotation value, False otherwise.

        Parameters
        - dir: direction to spin in, a DirectionType enum value or None.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion (Optional): If true, your program will wait
                                        until the motor reaches the target
                                        rotational value.
                                        If false, the program will continue
                                        after calling this function.
                                        By default, this parameter is true.
    """)
    @act
    def spin_for(self, dir: DirectionType,  # pylint: disable=redefined-builtin
                 rotation: NumType, rotationUnits: RotationUnits = RotationUnits.DEG,  # noqa: E501
                 velocity: Optional[NumType] = None,
                 velocityUnits: VelocityUnits = VelocityUnits.PCT,
                 waitForCompletion: bool = True, /) -> bool:
        """Spin motors for specified rotational angle."""

    @robotmesh_doc("""
        Turn on the motors and spin them for a given amount of time.

        Parameters
        - dir: direction to spin in, a DirectionType enum value or None.
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time value,
                     a TimeUnits enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value,
                         a VelocityUnits enum value.
    """)
    @act
    def spin_for_time(self,
                      dir: DirectionType,  # pylint: disable=redefined-builtin
                      time: NumType, timeUnits: TimeUnits = TimeUnits.SEC,
                      velocity: Optional[NumType] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin motors for specified time duration."""

    @robotmesh_doc("""
        Start spinning motors to an absolute target rotation.

        (but does not wait for the motors to reach that target)

        Parameters
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_to(self,
                      rotation: NumType,
                      rotationUnits: RotationUnits = RotationUnits.DEG,
                      velocity: Optional[NumType] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning motors to target rotational angle."""

    @robotmesh_doc("""
        Start spinning motors to a relative target rotation.

        (but does not wait for the motors to reach that target)

        Parameters
        - dir: direction to spin in, a DirectionType enum value or None.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_for(self,
                       dir: DirectionType,  # pylint: disable=redefined-builtin
                       rotation: NumType,
                       rotationUnits: RotationUnits = RotationUnits.DEG,  # noqa: E501
                       velocity: Optional[NumType] = None,
                       velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning motors for specified rotational angle."""

    @robotmesh_doc("""
        Determine if any motor in group is performing spin_for/spin_to command.

        Returns:
        True if any motors are spinning.
    """)
    @sense
    def is_spinning(self) -> bool:
        """Check whether one or some of the motors is/are still spinning."""

    @robotmesh_doc("""
        Determine if spin_for/spin_to command has reached its target position.

        Returns:
        False if any motor is on and is rotating to a target,
        True if all motors are done rotating to a target.
    """)
    @sense
    def is_done(self) -> bool:
        """Check whether all motors have finished spinning."""

    @robotmesh_doc("""
        Stop all motors using the default brake mode.

        Parameters
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop motors."""

    @robotmesh_doc("""
        Set the max torque of all motors as a percentage.

        Parameters
        - value: Sets the amount of torque (0 to 100%)
    """)
    @act
    def set_max_torque_percent(self, value: int, /):
        """Set max torque percentage level."""
        self.max_torque[TorqueUnits.PCT] = value

    @robotmesh_doc("""
        Set the max torque of all motors.

        Parameters
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
    """)
    @act
    def set_max_torque(self, value: NumType,
                       torqueUnits: TorqueUnits = TorqueUnits.NM, /):
        """Set max torque."""
        self.max_torque[torqueUnits] = value

    @robotmesh_doc("""
        Set the max torque of all motors.

        Parameters
        - value: Sets the amount of torque in Amps (max 1.2A)
    """)
    @act
    def set_max_torque_current(self, value: NumType, /):
        """Set max torque current."""
        # pylint: disable=attribute-defined-outside-init
        self.max_torque_current: NumType = value

    @robotmesh_doc("""
        Get the current rotation of the first motor in the group's encoder.

        Returns:
        Returns a float that represents the current rotation of the motor
        in the units defined in the parameter.

        Parameters
        - rotationUnits: The measurement unit for the rotation.
    """)
    @sense
    def rotation(self, rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:  # noqa: E501
        """Return motors' rotational angle."""

    @robotmesh_doc("""
        Get the current velocity of the first motor in the group.

        Returns:
        a float that represents the current velocity of the motor
        in the units defined in the parameter.

        Parameters
        - velocityUnits: The measurement unit for the velocity.
    """)
    @sense
    def velocity(self, velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:  # noqa: E501
        """Return motors' velocity."""

    @robotmesh_doc("""
        Get Current.
    """)
    @sense
    def current(self) -> NumType:
        """Return motors' electrical current."""
