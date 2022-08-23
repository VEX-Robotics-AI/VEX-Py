"""VEX Motor Group."""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self   # pylint: disable=no-name-in-module

from __vex.decor import act, sense

from vex import (BrakeType,
                 DirectionType,
                 Motor,
                 RotationUnits,
                 TimeUnits,
                 TorqueUnits,
                 VelocityUnits)


__all__: Sequence[str] = ('MotorGroup',)


class MotorGroup:   # pylint: disable=too-many-public-methods
    """VEX Motor Group."""

    def __init__(self, motors: list[Motor]):
        """
        Create a new motor group with specified motors.

        param:
        - motors: a list or tuple of motors in the group
        """
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

    def count(self) -> int:
        """
        Return the number of motors in the motor group.

        Returns:
        number of motors
        """
        return len(self.motors)

    @act
    def set_velocity(self, velocity: float, velocityUnits=VelocityUnits.PCT):
        """
        Set velocity of motor group based on parameters set in command.

        This command will not run the motor.
        Any subsequent call that does not contain a specified motor velocity
        will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for velocity,
                         a VelocityUnits enum value.
        """
        self.velocities[velocityUnits] = velocity

    @act
    def set_stopping(self, brakeType: BrakeType):
        """
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters:
        - brakeType: The stopping mode can be set
                     to BrakeType.COAST, BRAKE, or HOLD.
        """
        self.stopping: BrakeType = brakeType

    @act
    def reset_rotation(self):
        """Reset all motor encoders to the value of zero."""
        for motor in self.motors:
            for rotation_unit in self.rotations[motor]:
                self.rotations[motor][rotation_unit] = 0

    @act
    def set_rotation(self, value: float, rotationUnits=RotationUnits.DEG):
        """
        Set value of all motor encoders to value specified in parameter.

        Parameters
        - value: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation,
                         a RotationUnits enum value.
        """
        for motor in self.motors:
            self.rotations[motor][rotationUnits] = value

    @act
    def set_timeout(self, time: float, timeUnits=TimeUnits.SEC):
        """
        Set the timeout for the motor group.

        If the motor group does not reach its commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
        """
        self.timeouts[timeUnits] = time

    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC) -> float:
        """Return a timeout in given time units."""
        return self.timeouts[timeUnits]

    @sense
    def did_timeout(self) -> bool:
        """Return True if the last motor operation on any motor timed out."""

    @act
    def spin(
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turn on the motors and spins them.

        (in the specified direction and a specified velocity)

        Parameters:
        - dir: The direction to spin the motors,
               a DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
        """

    @act
    def spin_to(   # pylint: disable=too-many-arguments
            self,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
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
        """

    @act
    def spin_for(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
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
        """

    @act
    def spin_for_time(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            time: float, timeUnits: TimeUnits = TimeUnits.SEC,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turn on the motors and spin them for a given amount of time.

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time value,
                     a TimeUnits enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value,
                         a VelocityUnits enum value.
        """

    @act
    def start_spin_to(
            self,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Start spinning motors to an absolute target rotation.

        (but does not wait for the motors to reach that target)

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        """

    @act
    def start_spin_for(   # pylint: disable=too-many-arguments
            self, dir: DirectionType,   # pylint: disable=redefined-builtin
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Start spinning motors to a relative target rotation.

        (but does not wait for the motors to reach that target)

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        """

    @sense
    def is_spinning(self) -> bool:
        """
        Determine if any motor in group is performing spin_for/spin_to command.

        Returns:
        True if any motors are spinning.
        """

    @sense
    def is_done(self) -> bool:
        """
        Determine if spin_for/spin_to command has reached its target position.

        Returns:
        False if any motor is on and is rotating to a target,
        True if all motors are done rotating to a target.
        """

    @act
    def stop(self, brakeType: Optional[BrakeType] = None):
        """
        Stop all motors using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """

    @act
    def set_max_torque_percent(self, value: float):
        """
        Set the max torque of all motors as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
        """
        self.max_torque[TorqueUnits.PCT] = value

    @act
    def set_max_torque(
            self,
            value: float, torqueUnits: TorqueUnits = TorqueUnits.NM):
        """
        Set the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
        """
        self.max_torque[torqueUnits] = value

    @act
    def set_max_torque_current(self, value: float):
        """
        Set the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
        """
        # pylint: disable=attribute-defined-outside-init
        self.max_torque_current: float = value

    @sense
    def rotation(
            self,
            rotationUnits: RotationUnits = RotationUnits.DEG) -> float:
        """
        Get the current rotation of the first motor in the group's encoder.

        Returns:
        Returns a float that represents the current rotation of the motor
        in the units defined in the parameter.

        Parameters
        - rotationUnits: The measurement unit for the rotation.
        """

    @sense
    def velocity(
            self,
            velocityUnits: VelocityUnits = VelocityUnits.PCT) -> float:
        """
        Get the current velocity of the first motor in the group.

        Returns:
        a float that represents the current velocity of the motor
        in the units defined in the parameter.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.
        """

    @sense
    def current(self) -> float:
        """Get Current."""
