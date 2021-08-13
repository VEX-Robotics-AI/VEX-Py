from typing import Optional

from __decor import act, sense

from vex import (
    BrakeType,
    DirectionType,
    Motor,
    RotationUnits,
    TimeUnits,
    TorqueUnits,
    VelocityUnits
)


class MotorGroup:
    def __init__(self, motors: list[Motor]):
        """
        Creates a new motor group with specified motors

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

    def count(self) -> int:
        """
        return the number of motors in the motor group

        Returns:
        number of motors
        """
        return len(self.motors)

    @act
    def set_velocity(self, velocity: float, velocityUnits=VelocityUnits.PCT):
        """
        Sets the velocity of the motor group
        based on the parameters set in the command.

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
        Sets the stopping mode of the motor group
        by passing a brake mode as a parameter.

        Parameters:
        - brakeType: The stopping mode can be set
                     to BrakeType.COAST, BRAKE, or HOLD.
        """
        self.stopping: BrakeType = brakeType

    @act
    def reset_rotation(self):
        """
        Resets all motor encoders to the value of zero.
        """
        for motor in self.motors:
            for rotation_unit in self.rotations[motor]:
                self.rotations[motor][rotation_unit] = 0

    @act
    def set_rotation(self, value: float, rotationUnits=RotationUnits.DEG):
        """
        Sets the value of all motor encoders
        to the value specified in the parameter.

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
        Sets the timeout for the motor group.

        If the motor group does not reach its commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
        """
        self.timeouts[timeUnits] = time

    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC) -> float:
        """
        Returns:
        Returns a timeout in given time units
        """
        return self.timeouts[timeUnits]

    @sense
    def did_timeout(self) -> bool:
        """
        Returns:
        True if the last motor operation on any motor timed out
        """

    @act
    def spin(
            self, dir: DirectionType,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turn on the motors and spins them in the specified direction
        and a specified velocity.

        Parameters:
        - dir: The direction to spin the motors,
               a DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
        """

    @act
    def spin_to(
            self,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Turns on the motors and spin them to
        an absolute target rotation value at a specified velocity.

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
    def spin_for(
            self, dir: DirectionType,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Turn on the motors and spin them to a relative target rotation value
        at a specified velocity.

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
    def spin_for_time(
            self, dir: DirectionType,
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
        Starts spinning motors to an absolute target rotation
        but does not wait for the motors to reach that target.

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        """

    @act
    def start_spin_for(
            self, dir: DirectionType,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Starts spinning motors to a relative target rotation
        but does not wait for the motors to reach that target.

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
        Determines if any motor in the group
        is performing a spin_for/spin_to command.

        Returns:
        True if any motors are spinning.
        """

    @sense
    def is_done(self) -> bool:
        """
        Determines if a spin_for/spin_to command
        has reached its target position.

        Returns:
        False if any motor is on and is rotating to a target,
        True if all motors are done rotating to a target.
        """

    @act
    def stop(self, brakeType: Optional[BrakeType] = None):
        """
        Stops all motors using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """

    @act
    def set_max_torque_percent(self, value: float):
        """
        Sets the max torque of all motors as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
        """
        self.max_torque[TorqueUnits.PCT] = value

    @act
    def set_max_torque(
            self,
            value: float, torqueUnits: TorqueUnits = TorqueUnits.NM):
        """
        Sets the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
        """
        self.max_torque[torqueUnits] = value

    @act
    def set_max_torque_current(self, value: float):
        """
        Sets the max torque of all motors.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
        """
        self.max_torque_current: float = value

    @sense
    def rotation(
            self,
            rotationUnits: RotationUnits = RotationUnits.DEG) -> float:
        """
        Gets the current rotation of the first motor in the group's encoder.

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
        Gets the current velocity of the first motor in the group.

        Returns:
        a float that represents the current velocity of the motor
        in the units defined in the parameter.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.
        """

    @sense
    def current(self) -> float:
        ...
