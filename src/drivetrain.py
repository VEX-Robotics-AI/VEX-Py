"""VEX Drivetrain.

Robot Mesh VEX IQ Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacedrivetrain.html

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/namespacedrivetrain.html
"""


from collections.abc import Sequence
from typing import LiteralString, Optional, Self

from abm.decor import act, sense

from vex.motor import Motor
from vex.motor.brake import BrakeType
from vex.motor.direction import DirectionType
from vex.motor.turn import TurnType
from vex.motor.velocity import VelocityUnits
from vex.time.units import TimeUnits
from vex._common_enums.distance import DistanceUnits
from vex._common_enums.rotation import RotationUnits

from vex._util.doc import robotmesh_doc
from vex._util.type import NumType

from motor_group import MotorGroup


__all__: Sequence[LiteralString] = ('Drivetrain',)


DrivetrainMotorType = Motor | MotorGroup | list[Motor] | tuple[Motor]


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classdrivetrain_1_1_drivetrain.html
""")
class Drivetrain:  # pylint: disable=too-many-instance-attributes
    """Drivetrain."""

    @robotmesh_doc("""
        Create a new drivetrain object.

        Parameters
        - left_motor: the motor, motor group or a list/tuple of motors
                      driving the left side of the drivetrain
        - right_motor: the motor, motor group or a list/tuple of motors
                       driving the right side of the drivetrain
        - wheel_travel: circumference of the wheel type used
        - track_width: distance between the wheels on opposite sides
        - distanceUnits: unit for wheel_travel and track_with,
                         a DistanceUnits enum value
        - gear_ratio: external gear ratio, usually 1.0
    """)
    def __init__(
            self,
            left_motor: DrivetrainMotorType, right_motor: DrivetrainMotorType,
            wheel_travel: NumType = 200, track_width: NumType = 176,
            distanceUnits: DistanceUnits = DistanceUnits.MM,
            gear_ratio: NumType = 1, /):
        """Initialize Drivetrain."""
        self.left_motor: DrivetrainMotorType = left_motor
        self.right_motor: DrivetrainMotorType = right_motor
        self.wheel_travel: NumType = wheel_travel
        self.track_width: NumType = track_width
        self.distance_unit: DistanceUnits = distanceUnits
        self.gear_ratio: NumType = gear_ratio

        self.drive_velocities: dict[VelocityUnits, NumType] = \
            dict[VelocityUnits, NumType]()
        self.turn_velocities: dict[VelocityUnits, NumType] = \
            dict[VelocityUnits, NumType]()
        self.timeouts: dict[TimeUnits, NumType] = dict[TimeUnits, NumType]()
        self.stopping: Optional[BrakeType] = None

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, Drivetrain) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.wheel_travel == self.wheel_travel) and
                (other.track_width == self.track_width) and
                (other.distance_unit == self.distance_unit) and
                (other.gear_ratio == self.gear_ratio))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.left_motor, self.right_motor,
                     self.wheel_travel, self.track_width,
                     self.distance_unit, self.gear_ratio))

    @robotmesh_doc("""
        Turn the motors on and drives in the specified direction.

        Parameters
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def drive(self, directionType: DirectionType,
              velocity: Optional[NumType] = None,
              velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Drive."""

    @robotmesh_doc("""
        Drives for a specified distance.

        Parameters
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
        True if the drivetrain has reached the target distance, False otherwise
    """)
    @act
    def drive_for(
            self, directionType: DirectionType,
            distance: NumType, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[NumType] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Drive for specified distance."""

    @robotmesh_doc("""
        Start driving for a specified distance.

        Parameters
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - distance: distance to drive in
        - distanceUnits: unit for the distance parameter,
                         a DistanceUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def start_drive_for(
            self, directionType: DirectionType,
            distance: NumType, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[NumType] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start driving for specified distance."""

    @robotmesh_doc("""
        Turn the drivetrain left or right.

        Parameters
        - turnType: direction to turn in, left or right, a TurnType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def turn(self, turnType: TurnType,
             velocity: Optional[NumType] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Turn."""

    @robotmesh_doc("""
        Turn the drivetrain left or right until the specified angle is reached.

        Parameters
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

        Returns:
        True if the drivetrain has reached the target angle, False otherwise

        Reimplemented from drivetrain.Drivetrain.
    """)
    @act
    def turn_for(self, turnType: TurnType,
                 angle: NumType, rotationUnits: RotationUnits = RotationUnits.DEG,  # noqa: E501
                 velocity: Optional[NumType] = None,
                 velocityUnits: VelocityUnits = VelocityUnits.PCT,
                 waitForCompletion: bool = True, /) -> bool:
        """Turn for specified rotational angle."""

    @robotmesh_doc("""
        Start turning drivetrain left or right.

        (until specified angle is reached)

        Parameters
        - turnType: direction to turn in, left or right, a TurnType enum value
        - angle: sets the angle to turn
        - angleUnits: units for the angle parameter, a RotationUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value

        Reimplemented in smartdrive.Smartdrive.
    """)
    @act
    def start_turn_for(self, turnType: TurnType,
                       angle: NumType, angleUnits: RotationUnits = RotationUnits.DEG,  # noqa: E501
                       velocity: Optional[NumType] = None,
                       velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start turning for specified rotational angle."""

    @robotmesh_doc("""
        Drive in arcade mode.

        (normally corresponding to two controller joystick axis values)

        Parameters
        - drivePower: percent power to apply to driving, -100..100
        - turnPower: percent power to apply to turning, -100..100
    """)
    @act
    def arcade(self, drivePower: NumType, turnPower: NumType, /):
        """Arcade-drive."""

    @robotmesh_doc("""
        Stop the drive using a specified brake mode.

        Parameters
        - brakeType: brake mode, an BrakeType enum value.
                     If omitted, the value set in set_stopping is used.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop motors."""

    @robotmesh_doc("""
        Set the external gear ratio of the drivetrain.

        Parameters
        - gear_ratio: gear ratio value, usually 1.0
    """)
    @act
    def set_gear_ratio(self, gear_ratio: NumType, /):
        """Set gear ratio."""
        self.gear_ratio: NumType = gear_ratio

    @robotmesh_doc("""
        Set the velocity of the drive.

        Will not run the motors.
        Any subsequent call that does not contain a specified velocity
        will use this value.

        Parameters
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def set_drive_velocity(self, velocity: NumType,
                           velocityUnits: VelocityUnits = VelocityUnits.PCT, /):  # noqa: E501
        """Set driving velocity."""
        self.drive_velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set the velocity of the turn.

        Will not run the motors.

        Parameters
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def set_turn_velocity(self, velocity: NumType,
                          velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Set turning velocity."""
        self.turn_velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set the timeout for the drivetrain.

        If the drivetrain does not reach its' commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters
        - time: the amount of time.
        - timeUnits: unit for the time parameter, a TimeUnits enum value
    """)
    @act
    def set_timeout(self, time: NumType, timeUnits: TimeUnits = TimeUnits.SEC, /):  # noqa: E501
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
        Return True if last drivetrain operation timed out, False otherwise.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Check whether motors timed out."""

    @robotmesh_doc("""
        Return True if drivetrain is done driving/turning to specified target.

        False otherwise.

        Reimplemented in smartdrive.Smartdrive.
    """)
    @sense
    def is_done(self) -> bool:
        """Check whether both motors have finished driving/turning."""

    @robotmesh_doc("""
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters
        - brakeType: the stopping mode, a BrakeType enum value
                     (coast, brake, or hold).
    """)
    @act
    def set_stopping(self, brakeType: BrakeType, /):
        """Set motor stopping mode."""
        self.stopping: BrakeType = brakeType

    @robotmesh_doc("""
        Get the average current velocity of all motors.

        Returns:
        a float that represents the average current velocity

        Parameters
        - velocityUnits: The measurement unit for the velocity.
    """)
    @sense
    def velocity(self, velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:  # noqa: E501
        """Return motors' velocity."""

    @robotmesh_doc("""
        Get the electrical current of all motors.

        Returns:
        a float that represents the electrical current of the motor in Amps.
    """)
    @sense
    def current(self) -> float:
        """Return motors' electrical current."""
