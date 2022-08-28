"""VEX Smart Drivetrain."""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self   # pylint: disable=no-name-in-module

from abm.decor import act, sense

from drivetrain import Drivetrain, DrivetrainMotorType
from vex import (BrakeType,
                 DirectionType,
                 DistanceUnits,
                 Gyro,
                 RotationUnits,
                 TimeUnits,
                 TurnType,
                 VelocityUnits)


__all__: Sequence[str] = ('Smartdrive',)


class Smartdrive(Drivetrain):
    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """VEX Smart Drivetrain."""

    def __init__(   # pylint: disable=too-many-arguments
            self,
            left_motor: DrivetrainMotorType, right_motor: DrivetrainMotorType,
            gyro: Gyro,
            wheel_travel: float = 200, track_width: float = 176,
            distanceUnits: DistanceUnits = DistanceUnits.MM,
            gear_ratio: float = 1):
        """
        Create a new smartdrive object.

        Parameters:
        - left_motor: the motor, motor group or a list/tuple of motors
                      driving the left side of the drivetrain
        - right_motor: the motor, motor group or a list/tuple of motors
                       driving the right side of the drivetrain
        - gyro: the gyro or initial sensor used to determine orientation
        - wheel_travel: circumference of the wheel type used
        - track_width: distance between the wheels on opposite sides
        - distanceUnits: unit for wheel_travel and track_with,
                         a DistanceUnits enum value
        - gear_ratio: external gear ratio, usually 1.0
        """
        # pylint: disable=super-init-not-called

        self.left_motor: DrivetrainMotorType = left_motor
        self.right_motor: DrivetrainMotorType = right_motor
        self.gyro: Gyro = gyro
        self.wheel_travel: float = wheel_travel
        self.track_width: float = track_width
        self.distance_unit: DistanceUnits = distanceUnits
        self.gear_ratio: float = gear_ratio

        self.drive_velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.turn_velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.timeouts: dict[TimeUnits, float] = dict[TimeUnits, float]()
        self.stopping: Optional[BrakeType] = None

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, Smartdrive) and \
            (other.left_motor == self.left_motor) and \
            (other.right_motor == self.right_motor) and \
            (other.gyro == self.gyro) and \
            (other.wheel_travel == self.wheel_travel) and \
            (other.track_width == self.track_width) and \
            (other.distance_unit == self.distance_unit) and \
            (other.gear_ratio == self.gear_ratio)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.left_motor, self.right_motor,
                     self.gyro,
                     self.wheel_travel, self.track_width,
                     self.distance_unit, self.gear_ratio))

    @act
    def turn_to_heading(   # pylint: disable=too-many-arguments
            self,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Turn on the motors and rotate to a heading at the default velocity.

        Returns:
        True if the motor has reached the target rotation value.

        Parameters:
        - angle: Sets the angle to turn.
        - angleUnits: The measurement unit for the angle value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion	(Optional): If true, your program will wait
                                        until the motor reaches the target
                                        rotational value.
                                        If false, the program will continue
                                        after calling this function.
                                        By default, this parameter is true.
        """

    @act
    def turn_to_rotation(   # pylint: disable=too-many-arguments
            self,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """Turn to rotation."""

    @act
    def turn_for(   # pylint: disable=arguments-renamed,too-many-arguments
            self, turnType: TurnType,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Turn the drivetrain left or right until the specified angle is reached.

        Parameters:
        - turnType: direction to turn in, left or right, a TurnType enum value
        - angle: sets the angle to turn
        - rotationUnits: units for the angle parameter,
                         a RotationUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        - waitForCompletion: if True, your program will wait until
                             the motor reaches the target rotational value,
                             otherwise it will continue immediately.

        Returns
        True if the drivetrain has reached the target angle, False otherwise.

        Reimplemented from drivetrain.Drivetrain.
        """

    @act
    def start_turn_to_heading(
            self,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """Start turn to heading."""

    @act
    def start_turn_to_rotation(
            self,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """Start turn to rotation."""

    @act
    def start_turn_for(   # pylint: disable=too-many-arguments
            self, turnType: TurnType,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Start turning drivetrain left or right.

        (until specified angle is reached)

        Parameters:
        - turnType: direction to turn in, left or right, a TurnType enum value
        - angle: sets the angle to turn
        - angleUnits: units for the angle parameter, a RotationUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value

        Reimplemented from drivetrain.Drivetrain.
        """

    @sense
    def is_done(self) -> bool:
        """
        Check if turnToHeading, turnToRotation or turnFor is still running.

        Returns:
        True if the motor is on and is rotating to a target, False otherwise.

        Reimplemented from drivetrain.Drivetrain.
        """

    @act
    def drive(
            self, directionType: DirectionType,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turn the motors on and drives in the specified direction.

        Parameters:
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        """

    @act
    def drive_for(   # pylint: disable=too-many-arguments
            self, directionType: DirectionType,
            distance: float, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True) -> bool:
        """
        Drives for a specified distance.

        Parameters:
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - distance: distance to drive in
        - distanceUnits: unit for the distance parameter,
                         a DistanceUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        - waitForCompletion: if True, your program will wait until
                             the motor reaches the target rotational value,
                             otherwise it will continue immediately.

        Returns:
        True if the drivetrain has reached the target distance,
        False otherwise.
        """

    @act
    def start_drive_for(   # pylint: disable=too-many-arguments
            self, directionType: DirectionType,
            distance: float, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Start driving for a specified distance.

        Parameters:
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - distance: distance to drive in
        - distanceUnits: unit for the distance parameter,
                         a DistanceUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        """

    @act
    def turn(
            self, turnType: TurnType,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Turn the drivetrain left or right.

        Parameters:
        - turnType: direction to turn in, left or right, a TurnType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        """

    @act
    def arcade(self, drivePower: float, turnPower: float):
        """
        Drive in arcade mode.

        (normally corresponding to two controller joystick axis values)

        Parameters:
        - drivePower: percent power to apply to driving, -100..100
        - turnPower: percent power to apply to turning, -100..100
        """

    @act
    def stop(self, brakeType: Optional[BrakeType] = None):
        """
        Stop the drive using a specified brake mode.

        Parameters:
        - brakeType: brake mode, an BrakeType enum value.
                     If omitted, the value set in set_stopping is used.
        """

    @act
    def set_gear_ratio(self, gear_ratio: float):
        """
        Set the external gear ratio of the drivetrain.

        Parameters:
        - gear_ratio: gear ratio value, usually 1.0
        """
        self.gear_ratio: float = gear_ratio

    @act
    def set_drive_velocity(
            self,
            velocity: float, velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Set the velocity of the drive.

        Will not run the motors.
        Any subsequent call that does not contain a specified velocity
        will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        """
        self.drive_velocities[velocityUnits] = velocity

    @act
    def set_turn_velocity(
            self,
            velocity: float, velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """
        Set the velocity of the turn.

        Will not run the motors.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
        """
        self.turn_velocities[velocityUnits] = velocity

    @act
    def set_timeout(self, time: float, timeUnits: TimeUnits = TimeUnits.SEC):
        """
        Set the timeout for the drivetrain.

        If the drivetrain does not reach its' commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters:
        - time: the amount of time.
        - timeUnits: unit for the time parameter, a TimeUnits enum value
        """
        self.timeouts[timeUnits] = time

    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC) -> float:
        """Return a timeout in given time units."""
        return self.timeouts[timeUnits]

    @sense
    def did_timeout(self) -> bool:
        """Return True if last drivetrain operation timed out, False otherwise."""   # noqa: E501

    @act
    def set_stopping(self, brakeType: BrakeType):
        """
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters:
        - brakeType: the stopping mode,
                     a BrakeType enum value (coast, brake, or hold).
        """
        self.stopping: BrakeType = brakeType

    @sense
    def velocity(
            self,
            velocityUnits: VelocityUnits = VelocityUnits.PCT) -> float:
        """
        Get the average current velocity of all motors.

        Returns:
        a float that represents the average current velocity

        Parameters:
        - velocityUnits: The measurement unit for the velocity.
        """

    @sense
    def current(self) -> float:
        """
        Get the electrical current of all motors.

        Returns:
        a float that represents the electrical current of the motor in Amps.
        """

    @property
    def gyro(self) -> Gyro:
        """Gyro Sensor."""
        return self._gyro

    @gyro.setter
    def gyro(self, gyro: Gyro):
        self._gyro: Gyro = gyro
