from enum import IntEnum

from __decor import act, sense

from .abstract import Device


class BrakeType(IntEnum):
    """
    The defined units for brake values.
    """
    COAST: int = 0   # A brake unit that is defined as coast.
    BRAKE: int = 1   # A brake unit that is defined as brake.
    HOLD: int = 2   # A brake unit that is defined as hold.


class DirectionType(IntEnum):
    """
    The defined units for direction values.
    """
    FWD: int = 0   # A direction unit that is defined as forward.
    REV: int = 1   # A direction unit that is defined as backward.


class Motor(Device):
    def __init__ (self, index, reverse=False):
        """
        Creates a new motor object on the port specified
        and sets the reversed flag.

        Parameters:
        - index: The port index for this motor. The index is zero-based.
                 reverse: Sets the reverse flag for the new motor object.
        """
        pass

    @act
    def set_reversed(self, is_reversed):
        """
        Sets the motor mode to "reverse", which will make
        motor commands spin the motor in the opposite direction.

        Parameters:
        - is_reversed: If set to True, motor commands
                       spin the motor in the opposite direction.
        """
        pass

    @act
    def set_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        """
        Sets the velocity of the motor based on
        the parameters set in the command.
        This command will not run the motor.
        Any subsequent call that does not contain
        a specified motor velocity will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
        """
        pass

    @act
    def set_stopping(self, brakeType):
        """
        Sets the stopping mode of the motor by passing a brake mode as a parameter.

        Parameters:
        - brakeType: The stopping mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """
        pass

    @act
    def reset_rotation(self):
        """
        Resets the motor's encoder to the value of zero.
        """
        pass

    @act
    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        """
        Sets the value of the motor's encoder to the value specified in the parameter.

        Parameters:
        - value: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation,
                         a RotationUnits enum value.
        """
        pass

    @act
    def set_timeout(self, time, timeUnits=TimeUnits.SEC):
        """
        Sets the timeout for the motor.
        If the motor does not reach its commanded position prior
        to the completion of the timeout, the motor will stop.

        Parameters:
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
        """
        pass

    @sense
    def timeout(self, timeUnits: TimeUnits=TimeUnits.SEC) -> float:
        """
        Returns a timeout in given time units
        """
        pass

    @sense
    def did_timeout(self) -> bool:
        """
        Return True if the last motor operation timed out
        """
        pass

    @act
    def spin(self, dir, velocity=None, velocityUnits=VelocityUnits.PCT):
        """
        Turns on the motor and spins it in a
        specified direction and a specified velocity.

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
        """
        pass

    @act
    def spin_to(
        self,
        rotation,
        rotationUnits=RotationUnits.DEG,
        velocity=None,
        velocityUnits=VelocityUnits.PCT,
        waitForCompletion=True
    ):
        """
        Turns on the motor and spins it to an absolute target
        rotation value at a specified velocity.
        """
        pass

    @act
    def spin_for(
        self,
        dir,
        rotation,
        rotationUnits=RotationUnits.DEG,
        velocity=None,
        velocityUnits=VelocityUnits.PCT,
        waitForCompletion=True
    ) -> bool:
        """
        Turns on the motor and spins it to a relative target
        rotation value at a specified velocity.

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.

        Returns:
        Returns a Boolean that signifies when the motor has reached the target rotation value.
        """
        pass

    @act
    def spin_for_time(
        self,
        dir,
        time,
        timeUnits=TimeUnits.SEC,
        velocity=None,
        velocityUnits=VelocityUnits.PCT
    ):
        """
        Turns on the motor and spins it to a relative target
        time value at a specified velocity.

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        """
        pass

    @act
    def start_spin_to(
        self,
        rotation,
        rotationUnits=RotationUnits.DEG,
        velocity=None,
        velocityUnits=VelocityUnits.PCT
    ):
        """
        Starts spinning a motor to an absolute target
        rotation but does not wait for the motor to reach that target.
        """
        pass

    @act
    def start_spin_for(
        self,
        dir,
        rotation,
        rotationUnits=RotationUnits.DEG,
        velocity=None,
        velocityUnits=VelocityUnits.PCT
    ):
        """
        Starts spinning a motor to a relative target
        rotation but does not wait for the motor to reach that target.

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        """
        pass

    @sense
    def is_spinning(self) -> bool:
        """
        Determines if a spin_for/spin_to command is in progress.

        Returns:
        True if the motor is on and is rotating to a target,
        False if the motor is done rotating to a target.
        """
        pass

    @sense
    def is_done(self) -> bool:
        """
        Determines if a spin_for/spin_to command
        has reached its target position.

        Returns:
        False if the motor is on and is rotating
        to a target, True if the motor is done rotating to a target.
        """
        pass

    @act
    def stop(self, brakeType=None):
        """
        Stops the motor using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """
        pass

    @act
    def set_max_torque_percent(self, value):
        """
        Sets the max torque of the motor as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
        """
        pass

    @act
    def set_max_torque(self, value, torqueUnits=TorqueUnits.NM):
        """
        Sets the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
        """
        pass

    @act
    def set_max_torque_current(self, value):
        """
        Sets the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
        """
        pass

    @sense
    def rotation(self, rotationUnits=RotationUnits.DEG) -> float:
        """
        Gets the current rotation of the motor's encoder.

        Parameters:
        rotationUnits: The measurement unit for the rotation.

        Returns:
        a float that represents the current rotation of
        the motor in the units defined in the parameter.
        """
        pass

    @sense
    def velocity(
            self,
            velocityUnits=VelocityUnits.PCT) -> float:
        """
        Gets the current velocity of the motor.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.

        Returns:
        a float that represents the current velocity
        of the motor in the units defined in the parameter.
        """
        pass

    @sense
    def current(self) -> float:
        """
        Gets the electrical current of the motor.

        Returns:
        a float that represents the electrical current of the motor in Amps.
        """
        pass


class TorqueUnits(IntEnum):
    """
    The measurement units for torque values.
    """
    NM: int = 0   # A torque unit that is measured in Newton Meters.
    IN_LB: int = 1   # A torque unit that is measured in Inch Pounds.


class TurnType(IntEnum):
    """
    Left or right turn.
    """
    LEFT: int = 0
    RIGHT: int = 1


class VelocityUnits(IntEnum):
    """
    The measurement units for velocity values.
    """
    PCT: int = 0   # A velocity unit that is measured in percentage.
    RPM: int = 1   # A velocity unit that is measured in rotations per minute.
    DPS: int = 2   # A velocity unit that is measured in degrees per second.
    RAW: int = 99   # A velocity unit that is measured in raw data form.
