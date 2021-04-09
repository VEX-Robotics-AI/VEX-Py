from enum import IntEnum
from typing import Optional

from __decor import act, sense

from .abstract import Device
from .port import Ports
from .time import TimeUnits
from .units_common import RotationUnits


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


class TorqueUnits(IntEnum):
    """
    The measurement units for torque values.
    """
    NM: int = 0   # A torque unit that is measured in Newton Meters.
    IN_LB: int = 1   # A torque unit that is measured in Inch Pounds.
    PCT: int = 2


class VelocityUnits(IntEnum):
    """
    The measurement units for velocity values.
    """
    PCT: int = 0   # A velocity unit that is measured in percentage.
    RPM: int = 1   # A velocity unit that is measured in rotations per minute.
    DPS: int = 2   # A velocity unit that is measured in degrees per second.
    RAW: int = 99   # A velocity unit that is measured in raw data form.


class Motor(Device):
    def __init__(self, index: Ports, reverse: bool = False):
        """
        Creates a new motor object on the port specified
        and sets the reversed flag.

        Parameters:
        - index: The port index for this motor. The index is zero-based.
        - reverse: Sets the reverse flag for the new motor object.
        """
        self.port: Ports = index
        self.reverse: bool = reverse

        self.velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.stopping: Optional[BrakeType] = None
        self.rotations: dict[RotationUnits, float] = \
            dict[RotationUnits, float]()
        self.timeouts: dict[TimeUnits, float] = dict[TimeUnits, float]()

        self.max_torque: dict[TorqueUnits, float] = dict[TorqueUnits, float]()

    @act
    def set_reversed(self, is_reversed: bool):
        """
        Sets the motor mode to "reverse", which will make
        motor commands spin the motor in the opposite direction.

        Parameters:
        - is_reversed: If set to True, motor commands
                       spin the motor in the opposite direction.
        """
        self.reverse: bool = is_reversed

    @act
    def set_velocity(
            self,
            velocity: float, velocityUnits: VelocityUnits = VelocityUnits.PCT):
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
        self.velocities[velocityUnits]: float = velocity

    @act
    def set_stopping(self, brakeType: BrakeType):
        """
        Sets the stopping mode of the motor
        by passing a brake mode as a parameter.

        (note this will stop the motor if it's spinning)

        Parameters:
        - brakeType: The stopping mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """
        self.stopping: BrakeType = brakeType

    @act
    def reset_rotation(self):
        """
        Resets the motor's encoder to the value of zero.
        """
        for rotation_unit in self.rotations:
            self.rotations[rotation_unit]: float = 0

    @act
    def set_rotation(
            self,
            value: float, rotationUnits: RotationUnits = RotationUnits.DEG):
        """
        Sets the value of the motor's encoder
        to the value specified in the parameter.

        Parameters:
        - value: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation,
                         a RotationUnits enum value.
        """
        self.rotations[rotationUnits]: float = value

    @act
    def set_timeout(self, time: float, timeUnits: TimeUnits = TimeUnits.SEC):
        """
        Sets the timeout for the motor.
        If the motor does not reach its commanded position prior
        to the completion of the timeout, the motor will stop.

        Parameters:
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
        """
        self.timeouts[timeUnits]: float = time

    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC) -> float:
        """
        Returns a timeout in given time units
        """
        return self.timeouts[timeUnits]

    @sense
    def did_timeout(self) -> bool:
        """
        Return True if the last motor operation timed out
        """

    @act
    def spin(
            self, dir: DirectionType,
            velocity: float, velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turns on the motor and spins it in a
        specified direction and a specified velocity.

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
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
        Turns on the motor and spins it to an absolute target
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
        """

    @act
    def spin_for(
            self, dir: DirectionType,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Turns on the motor and spins it to a relative target
        rotation value at a specified velocity.

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
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
        Returns a Boolean that signifies when the motor
        has reached the target rotation value.
        """

    @act
    def spin_for_time(
            self, dir: DirectionType,
            time: str, timeUnits: TimeUnits = TimeUnits.SEC,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
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

    @act
    def start_spin_to(
            self,
            rotation: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Starts spinning a motor to an absolute target
        rotation but does not wait for the motor to reach that target.

        Params:
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
        Starts spinning a motor to a relative target
        rotation but does not wait for the motor to reach that target.

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
        Determines if a spin_for/spin_to command is in progress.

        Returns:
        True if the motor is on and is rotating to a target,
        False if the motor is done rotating to a target.
        """

    @sense
    def is_done(self) -> bool:
        """
        Determines if a spin_for/spin_to command
        has reached its target position.

        Returns:
        False if the motor is on and is rotating
        to a target, True if the motor is done rotating to a target.
        """

    @act
    def stop(self, brakeType: Optional[BrakeType] = None):
        """
        Stops the motor using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
        """

    @act
    def set_max_torque_percent(self, value: float):
        """
        Sets the max torque of the motor as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
        """
        self.max_torque[TorqueUnits.PCT]: float = value

    @act
    def set_max_torque(
            self,
            value: float, torqueUnits: TorqueUnits = TorqueUnits.NM):
        """
        Sets the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
        """
        self.max_torque[torqueUnits]: float = value

    @act
    def set_max_torque_current(self, value: float):
        """
        Sets the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
        """
        self.max_torque_current: float = value

    @sense
    def rotation(
            self,
            rotationUnits: RotationUnits = RotationUnits.DEG) -> float:
        """
        Gets the current rotation of the motor's encoder.

        Parameters:
        rotationUnits: The measurement unit for the rotation.

        Returns:
        a float that represents the current rotation of
        the motor in the units defined in the parameter.
        """

    @sense
    def velocity(
            self,
            velocityUnits: VelocityUnits = VelocityUnits.PCT) -> float:
        """
        Gets the current velocity of the motor.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.

        Returns:
        a float that represents the current velocity
        of the motor in the units defined in the parameter.
        """

    @sense
    def current(self) -> float:
        """
        Gets the electrical current of the motor.

        Returns:
        a float that represents the electrical current of the motor in Amps.
        """


class TurnType(IntEnum):
    """
    Left or right turn.
    """
    LEFT: int = 0
    RIGHT: int = 1
