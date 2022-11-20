"""VEX Motor Group.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacemotor__group.html
"""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self

from abm.decor import act, sense

from vex import (BrakeType,
                 DirectionType,
                 Motor,
                 RotationUnits,
                 TimeUnits,
                 TorqueUnits,
                 VelocityUnits)

from vex.util.doc import robotmesh_doc


__all__: Sequence[str] = ('MotorGroup',)


# TODO: add VEXcode
@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classmotor__group_1_1_motor_group.html
""")
class MotorGroup:   # pylint: disable=too-many-public-methods
    """VEX Motor Group."""

    @robotmesh_doc("""
        Create a new motor group with specified motors.

        param:
        - motors: a list or tuple of motors in the group
    """)
    def __init__(self, motors: list[Motor], /):
        """Initialize Motor Group."""
        self.motors: list[Motor] = motors
        self.rotations: dict[Motor, dict[RotationUnits, float]] = \
            {motor: {} for motor in motors}

        self.velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.stopping: Optional[BrakeType] = None
        self.timeouts: dict[TimeUnits, float] = dict[TimeUnits, float]()
        self.max_torque: dict[TorqueUnits, float] = dict[TorqueUnits, float]()

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, MotorGroup) and \
            (set(other.motors) == set(self.motors))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash(set(self.motors))

    @robotmesh_doc("""
        Return the number of motors in the motor group.

        Returns:
        number of motors
    """)
    def count(self) -> int:
        """Count number of Motors."""
        return len(self.motors)

    @robotmesh_doc("""
        Set velocity of motor group based on parameters set in command.

        This command will not run the motor.
        Any subsequent call that does not contain a specified motor velocity
        will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for velocity,
                         a VelocityUnits enum value.
    """)
    @act
    def set_velocity(self, velocity: float, velocityUnits=VelocityUnits.PCT, /):   # noqa: E501
        """Set Motor Velocity."""
        self.velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters:
        - brakeType: The stopping mode can be set
                     to BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def set_stopping(self, brakeType: BrakeType, /):
        """Set Motor Stopping Mode."""
        self.stopping: BrakeType = brakeType

    @robotmesh_doc("""
        Reset all motor encoders to the value of zero.
    """)
    @act
    def reset_rotation(self):
        """Reset Motors' Cumulative Rotation Angle Value to 0."""
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
    def set_rotation(self, value: float, rotationUnits=RotationUnits.DEG, /):
        """Set Motor's Cumulative Rotation Angle to certain value."""
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
    def set_timeout(self, time: float, timeUnits=TimeUnits.SEC, /):
        """Set Motor Timeout."""
        self.timeouts[timeUnits] = time

    @robotmesh_doc("""
        Return a timeout in given time units.
    """)
    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC, /) -> float:
        """Return Motor Timeout."""
        return self.timeouts[timeUnits]

    @robotmesh_doc("""
        Return True if the last motor operation on any motor timed out.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Check whether Motors timed out."""

    @robotmesh_doc("""
        Turn on the motors and spins them.

        (in the specified direction and a specified velocity)

        Parameters:
        - dir: The direction to spin the motors,
               a DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
    """)
    @act
    def spin(self, dir: DirectionType,   # pylint: disable=redefined-builtin
             velocity: Optional[float] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin Motors."""

    @robotmesh_doc("""
        Turn on the motors and spin them.

        (to an absolute target rotation value at a specified velocity)

        Returns:
        Returns a Boolean that signifies when
        the motors have reached the target rotation value.

        Parameters:
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
    def spin_to(   # pylint: disable=too-many-arguments
            self,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Spin Motors to certain target cumulative Rotation Angle Value."""

    @robotmesh_doc("""
        Turn on the motors and spin them.

        (to a relative target rotation value at a specified velocity)

        Returns:
        True if motors have reached the target rotation value, False otherwise.

        Parameters:
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
    def spin_for(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Spin Motors for certain Rotation Angle Value."""

    @robotmesh_doc("""
        Turn on the motors and spin them for a given amount of time.

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time value,
                     a TimeUnits enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value,
                         a VelocityUnits enum value.
    """)
    @act
    def spin_for_time(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            time: float, timeUnits: TimeUnits = TimeUnits.SEC,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin Motors for certain time duration."""

    @robotmesh_doc("""
        Start spinning motors to an absolute target rotation.

        (but does not wait for the motors to reach that target)

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_to(self,
                      rotation: float,
                      rotationUnits: RotationUnits = RotationUnits.DEG,
                      velocity: Optional[float] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning Motors to target cumulative Rotation Angle Value."""

    @robotmesh_doc("""
        Start spinning motors to a relative target rotation.

        (but does not wait for the motors to reach that target)

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_for(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning Motors for certain Rotation Angle Value."""

    @robotmesh_doc("""
        Determine if any motor in group is performing spin_for/spin_to command.

        Returns:
        True if any motors are spinning.
    """)
    @sense
    def is_spinning(self) -> bool:
        """Check whether Motors are spinning."""

    @robotmesh_doc("""
        Determine if spin_for/spin_to command has reached its target position.

        Returns:
        False if any motor is on and is rotating to a target,
        True if all motors are done rotating to a target.
    """)
    @sense
    def is_done(self) -> bool:
        """Check whether Motors have finished spinning."""

    @robotmesh_doc("""
        Stop all motors using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop Motors."""

    @robotmesh_doc("""
        Set the max torque of all motors as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
    """)
    @act
    def set_max_torque_percent(self, value: float, /):
        """Set Max Torque Percent."""
        self.max_torque[TorqueUnits.PCT] = value

    @robotmesh_doc("""
        Set the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
    """)
    @act
    def set_max_torque(self, value: float,
                       torqueUnits: TorqueUnits = TorqueUnits.NM, /):
        """Set Max Torque Percent."""
        self.max_torque[torqueUnits] = value

    @robotmesh_doc("""
        Set the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
    """)
    @act
    def set_max_torque_current(self, value: float, /):
        """Set Max Torque Current."""
        # pylint: disable=attribute-defined-outside-init
        self.max_torque_current: float = value

    @robotmesh_doc("""
        Get the current rotation of the first motor in the group's encoder.

        Returns:
        Returns a float that represents the current rotation of the motor
        in the units defined in the parameter.

        Parameters
        - rotationUnits: The measurement unit for the rotation.
    """)
    @sense
    def rotation(self, rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:   # noqa: E501
        """Return Motors' Cumulative Rotation Angle."""

    @robotmesh_doc("""
        Get the current velocity of the first motor in the group.

        Returns:
        a float that represents the current velocity of the motor
        in the units defined in the parameter.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.
    """)
    @sense
    def velocity(self, velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:   # noqa: E501
        """Return Motors' Velocity."""

    @robotmesh_doc("""
        Get Current.
    """)
    @sense
    def current(self) -> float:
        """Return Motors' Electrical Current."""
