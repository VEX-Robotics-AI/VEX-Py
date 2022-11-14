"""Drivetrain.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacedrivetrain.html
"""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self

from abm.decor import act, sense

from motor_group import MotorGroup
from vex import (BrakeType,
                 DirectionType,
                 DistanceUnits,
                 Motor,
                 RotationUnits,
                 TimeUnits,
                 TurnType,
                 VelocityUnits,)
from vex.units_common.electric import ElectricCurrentUnits
from vex.util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = ('Drivetrain',)


DrivetrainMotorType = Motor | MotorGroup | list[Motor] | tuple[Motor]


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classdrivetrain_1_1_drivetrain.html
""")
@vexcode_doc("""
""")
class Drivetrain:
    # pylint: disable=too-many-instance-attributes
    """VEX Drivetrain."""

    @robotmesh_doc("""
        Create a new drivetrain object.

        Parameters:
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
    def __init__(   # pylint: disable=too-many-arguments
            self,
            left_motor: DrivetrainMotorType, right_motor: DrivetrainMotorType,
            wheel_travel: float = 200, track_width: float = 176,
            distanceUnits: DistanceUnits = DistanceUnits.MM,
            gear_ratio: float = 1, /):
        """Initialize Drivetrain."""
        self.left_motor: DrivetrainMotorType = left_motor
        self.right_motor: DrivetrainMotorType = right_motor
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
        return (isinstance(other, Drivetrain) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.wheel_travel == self.wheel_travel) and
                (other.track_width == self.track_width) and
                (other.distance_unit == self.distance_unit) and
                (other.gear_ratio == self.gear_ratio))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.left_motor, self.right_motor,
                     self.wheel_travel, self.track_width,
                     self.distance_unit, self.gear_ratio))

    @robotmesh_doc("""
        Turn the motors on and drives in the specified direction.

        Parameters:
        - directionType: direction to drive in, forward or reverse,
                         a DirectionType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @vexcode_doc("""
        Moves the Drivetrain forever in the direction specified inside the parentheses.

        All Drivetrain motors run forward or in reverse at the velocity set using
        the Drivetrain's Set Drive Velocity command. The default velocity is 50%.

        Negative values will cause the Drivetrain to drive forward with a REVERSE input
        and in reverse with a FORWARD input.
            drivetrain.drive(DIRECTION)

        The Drive command will run the Drivetrain forever, until a new drivetrain command is used,
        or the program is stopped.

        Use the FORWARD argument in all-capital letters to move the Drivetrain forward.
            drivetrain.drive(FORWARD)
        Use the REVERSE argument in all-capital letters to move the Drivetrain in reverse.
            drivetrain.drive(REVERSE)
    """)
    @act
    def drive(self, directionType: DirectionType,
              velocity: Optional[float] = None,
              velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Drive."""

    @robotmesh_doc("""
        Drive for a specified distance.

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
    @vexcode_doc("""
        Moves the Drivetrain for a given distance.
        All Drivetrain motors run forward or in reverse at the velocity set by the Drivetrain's Set Drive Velocity
        command. After the Drivetrain has moved the specified distance the Drivetrain will stop.
            drivetrain.drive_for(DIRECTION, DISTANCE, UNITS)

        Set how far the Drivetrain will move by entering at least three valid arguments inside of the parentheses,
        separated by commas.
        - The first argument specifies the direction. Valid inputs are either FORWARD or REVERSE in all capital letters.
        - The second argument specifies the distance that the IQ Robot should drive.
        - The third argument specifies the unit of measurement that should be used.
            Valid inputs are either INCHES or MM (millimeters) in all-capital letters.

        The DISTANCE parameter accepts numeric values.
        Negative values will cause the IQ Robot to drive in the opposite of the input DIRECTION.
            drivetrain.drive_for(REVERSE, 5.0, INCHES)

        The Drive For command is by default a blocking command.
        It will prevent subsequent commands from executing until the Drivetrain movement has completed.

        This example shows the Drive For command being used with a variable as a distance.
        The IQ Robot will drive 200 MM forward.
            distance_variable = 200
            drivetrain.drive_for(FORWARD, distance_variable, MM)
    """)
    @act
    def drive_for(   # pylint: disable=too-many-arguments
            self, directionType: DirectionType,
            distance: float, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Drive a distance."""

    @robotmesh_doc("""
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
    """)
    @act
    def start_drive_for(   # pylint: disable=too-many-arguments
            self, directionType: DirectionType,
            distance: float, distanceUnits: DistanceUnits = DistanceUnits.MM,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start driving a distance."""

    @robotmesh_doc("""
        Turn the drivetrain left or right.

        Parameters:
        - turnType: direction to turn in, left or right, a TurnType enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @vexcode_doc("""
        Turns the Drivetrain to the right or left indefinitely.
            drivetrain.turn(DIRECTION)
        The Turn command will rotate the Drivetrain in the given direction forever until
        a new Drivetrain command is used, or until the program is stopped.

        Use the LEFT argument in all-capital letters to turn the Drivetrain to the left.
            drivetrain.turn(LEFT)
        Use the RIGHT argument in all-capital letters to turn the Drivetrain to the right.
            drivetrain.turn(RIGHT)

        In this example, the robot will drive forward 200 MM before turning right indefinitely.
            drivetrain.drive_for(FORWARD, 200, MM)
            drivetrain.turn(RIGHT)
    """)
    @act
    def turn(self, turnType: TurnType,
             velocity: Optional[float] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Turn."""

    @robotmesh_doc("""
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

        Returns:
        True if the drivetrain has reached the target angle, False otherwise

        Reimplemented in smartdrive.Smartdrive.
    """)
    @vexcode_doc("""
        Turns the Drivetrain in the specified direction for a set number of degrees.
            drivetrain.turn_for(DIRECTION, ANGLE, DEGREES)
        - The first argument specifies the turn direction: LEFT or RIGHT, written in all-capital letters.
        - The second argument specifies the turn angle as a numeric value; this can be any number or numeric variable.
        - The third argument is the turn units. This should be set as DEGREES in all-capital letters.

        The Turn For command is by default a blocking command.
        It prevents any proceeding code from executing until the Drivetrain has completed its turn.

        Optional parameter:
            If the fourth argument is set to wait=False,
            proceeding commands will be allowed to execute even before the Drivetrain has completed its turn.
                drivetrain.turn_for(LEFT, 90, DEGREES, wait=False)

        This example will turn the IQ Robot 270 degrees to the right.
            drivetrain.turn_for(RIGHT, 270, DEGREES)
    """)
    @act
    def turn_for(   # pylint: disable=too-many-arguments
            self, turnType: TurnType,
            angle: float, rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Turn an angle."""

    @robotmesh_doc("""
        Start turning the drivetrain left or right.

        (until the specified angle is reached)

        Parameters:
        - turnType: direction to turn in, left or right, a TurnType enum value
        - angle: sets the angle to turn
        - angleUnits: units for the angle parameter, a RotationUnits enum value
        - velocity: set velocity of the motors
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value

        Reimplemented in smartdrive.Smartdrive.
    """)
    @act
    def start_turn_for(   # pylint: disable=too-many-arguments
            self, turnType: TurnType,
            angle: float, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start turning an angle."""

    @vexcode_doc("""
        Turns a Drivetrain to a specific heading, when using a Gyro or Inertial Sensor.
            drivetrain.turn_to_heading(HEADING, DEGREES)

        The Turn to Heading command can be used to turn the Drivetrain to any given clockwise
        or counter-clockwise positive heading, depending on whether a Gyro
        or Inertial Sensor is configured with the Drivetrain.

        Based on the current heading, Turn to Heading will determine the shortest direction to turn.
        The HEADING parameter accepts numeric values in the range of 0.00 to 359.99 .
        The second parameter should be set to DEGREES.

        Optionals parameters:
            You can set wait=False as a third parameter to prevent the Turn to Heading command
            from blocking proceeding commands from executing until the Drivetrain turn has completed.
                drivetrain.turn_to_heading(180.0, DEGREES, wait=False)

        This example will cause the Drivetrain to make four turns:
            drivetrain.turn_to_heading(45.0, DEGREES)   # Right to 45 degrees
            drivetrain.turn_to_heading(90.0, DEGREES)   # Right to 90 degrees
            drivetrain.turn_to_heading(270.0, DEGREES)  # Right to 270 degrees
            drivetrain.turn_to_heading(180.0, DEGREES)  # Left to 180 degrees
        (The direction descriptions below are based on a clockwise positive heading,
        with the IQ (2nd generation) Brain's Inertial Sensor configured with the Drivetrain)
        The Turn to Heading command will by default block proceeding commands until the Drivetrain turn has completed.
    """)
    @act
    def turn_to_heading(self, heading: float, units: RotationUnits = RotationUnits.DEG):
        """Turns a Drivetrain to a specific heading, when using a Gyro or Inertial Sensor."""

    @vexcode_doc("""
        Turns the Drivetrain to a specific angle of rotation when used with a Gyro or Inertial Sensor.
            drivetrain.turn_to_rotation(ROTATION, DEGREES)

        The Turn to Rotation command can be used to turn the Drivetrain to an absolute rotation value.

        Depending on whether the Drivetrain is configured with a Gyro or Inertial Sensor,
        rotation values can either be counter-clockwise positive (Gyro), or clockwise positive (Inertial).

        Based on the current rotation of the Drivetrain, Turn to Rotation will determine which direction to turn.

        The ROTATION parameter can accept numeric values.
        Numeric values are not limited to the range of 0 - 359.99 degrees.
        Turns will be absolute and may cause the robot to rotate more than once if necessary.

        Optionals parameters:
            You can set a third parameter to wait=False to prevent the Turn to Rotation command
            from blocking proceeding commands until the Drivetrain turn is completed.
                drivetrain.turn_to_rotation(180.0, DEGREES, wait=False)

        This example will cause the Drivetrain to make four turns:
            drivetrain.turn_to_rotation(90.0, DEGREES)  # Right (clockwise) to 90 degrees
            drivetrain.turn_to_rotation(180, DEGREES)   # Right (clockwise) to 180 degrees
            drivetrain.turn_to_rotation(-45, DEGREES)   # Left (counter-clockwise) to -45 degrees
            drivetrain.turn_to_rotation(0, DEGREES)     # Right (clockwise) to 0 degrees

        (The direction descriptions above are aligned with an IQ (2nd generation) Brain's Inertial Sensor
        being configured with the Drivetrain)
        The Turn to Rotationcommand will by default block proceeding commands until the Drivetrain turn has completed.
    """)
    @act
    def turn_to_rotation(self, rotation: float, units: RotationUnits = RotationUnits.DEG):
        """Turns the Drivetrain to a specific angle of rotation when used with a Gyro or Inertial Sensor."""

    @robotmesh_doc("""
        Drive in arcade mode.

        (normally corresponding to two controller joystick axis values)

        Parameters:
        - drivePower: percent power to apply to driving, -100..100
        - turnPower: percent power to apply to turning, -100..100
    """)
    @act
    def arcade(self, drivePower: float, turnPower: float, /):
        """Arcade-drive."""

    @robotmesh_doc("""
        Stop the drive using a specified brake mode.

        Parameters:
        - brakeType: brake mode, an BrakeType enum value.
                     If omitted, the value set in set_stopping is used.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop driving."""

    @robotmesh_doc("""
        Set the external gear ratio of the drivetrain.

        Parameters:
        - gear_ratio: gear ratio value, usually 1.0
    """)
    @act
    def set_gear_ratio(self, gear_ratio: float, /):
        """Set Gear Ratio."""
        self.gear_ratio: float = gear_ratio

    @robotmesh_doc("""
        Set the velocity of the drive.

        Will not run the motors.
        Any subsequent call that does not contain a specified velocity
        will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def set_drive_velocity(self,
                           velocity: float,
                           velocityUnits: VelocityUnits = VelocityUnits.PCT, /):   # noqa: E501
        """Set Driving Velocity."""
        self.drive_velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set the velocity of the turn.

        Will not run the motors.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: unit for the velocity parameter,
                         a VelocityUnits enum value
    """)
    @act
    def set_turn_velocity(self,
                          velocity: float,
                          velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Set Turning Velocity."""
        self.turn_velocities[velocityUnits] = velocity

    @robotmesh_doc("""
        Set the timeout for the drivetrain.

        If the drivetrain does not reach its' commanded position
        prior to the completion of the timeout, the motors will stop.

        Parameters:
        - time: the amount of time.
        - timeUnits: unit for the time parameter, a TimeUnits enum value
    """)
    @act
    def set_timeout(self, time: float, timeUnits: TimeUnits = TimeUnits.SEC, /):   # noqa: E501
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
        Return True if last drivetrain operation timed out, False otherwise.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Check whether motors timed out."""

    @vexcode_doc("""
        Reports if the Drivetrain is currently moving.
            drivetrain.is_moving()
        Drive Is Moving reports True when the Drivetrain's motors are moving.
        Drive Is Moving reports False when the Drivetrain's motors are stopped.
        Note: This command will always return false if the Drivetrain is moving because of
        a drivetrain.drive or drivetrain.turn command (which do not specify a set distance to drive).
    """)
    @sense
    def is_moving(self) -> bool:
        """Reports if the Drivetrain is currently moving."""

    @robotmesh_doc("""
        Return True if drivetrain is done driving/turning to specified target.

        False otherwise.

        Reimplemented in smartdrive.Smartdrive.
    """)
    @sense
    def is_done(self) -> bool:
        """Check whether Drivetrain has finished driving/turning."""

    @robotmesh_doc("""
        Set stopping mode of motor group by passing brake mode as parameter.

        Parameters:
        - brakeType: the stopping mode, a BrakeType enum value
                     (coast, brake, or hold).
    """)
    @act
    def set_stopping(self, brakeType: BrakeType, /):
        """Set Motor Stopping Mode."""
        self.stopping: BrakeType = brakeType

    @vexcode_doc("""
        Sets the Drivetrain's Inertial or Gyro Sensor to the specified heading.
            drivetrain.set_heading(HEADING, DEGREES)

        The Drivetrain's Set Heading command can be used to set the Drivetrain's heading to a specified value.
        This command can be used to reset the orientation of the Drivetrain's Inertial
        or Gyro Sensor when the heading is set to a value of 0.

        Set Heading accepts a number value between 0 and 360 as it's first argument,
        and DEGREES written in all-capital letters as it's second argument.

        This example sets the Drivetrain heading to 90 degrees.
        Since the heading of the IQ Robot is set to 90 degrees, the subsequent Drivetrain's Turn
        to Heading command will not cause the robot to turn as its current heading is already 90 degrees.
            drivetrain.set_heading(90, DEGREES)
            drivetrain.turn_to_heading(90, DEGREES)
    """)
    @act
    def set_heading(self, heading: float, units: RotationUnits = RotationUnits.DEG):
        """Sets the Drivetrain's Inertial or Gyro Sensor to the specified heading."""

    @vexcode_doc("""
        Reports the direction that the Drivetrain is facing by using the Gyro
        or Inertial Sensor's current angular position.
            drivetrain.heading(DEGREES)

        Drive heading reports a range from 0.00 to 359.99 degrees.
        When the Drivetrain is configured with a Gyro Sensor,
        the Drive Heading command reports an increase in heading when rotating counter-clockwise.
        Alternatively, if the Drivetrain is configured with the IQ (2nd generation) Brain's Inertial Sensor,
        the Drive Heading command reports an increase in heading when rotating clockwise.
    """)
    @sense
    def heading(self, units: RotationUnits = RotationUnits.DEG) -> float:
        """Reports the direction that the Drivetrain is facing."""

    @vexcode_doc("""
        Sets the Drivetrain's Inertial or Gyro Sensor to a specified rotation.
            drivetrain.set_rotation(ROTATION, DEGREES)

        The Drivetrain's Set Rotation command can be used to set the Drivetrain's
        angle of rotation to any given positive or negative value.
        - The ROTATION parameter can accept numeric values.
        - The ROTATION parameter does not have a limit of 0-359 degrees.

        This example will turn the robot a total of 210 degrees if the Drivetrain
        is configured with the IQ (2nd generation) Brain's Inertial Sensor.
            drivetrain.turn_to_rotation(120, DEGREES)
            drivetrain.set_rotation(-45, DEGREES)
            drivetrain.turn_to_rotation(45, DEGREES)
        * Turn right (clockwise) to rotation 120 degrees.
        * Set the robot's current position as rotation of -45 degrees.
        * Turn right (clockwise) an additional 90 degrees (-45 degrees to +45 degrees)
        based on the set rotation value from the previous command.
    """)
    @act
    def set_rotation(self, rotation: float, units: RotationUnits = RotationUnits.DEG):
        """Sets the Drivetrain's Inertial or Gyro Sensor to a specified rotation."""

    @vexcode_doc("""
        Reports the Drivetrain's angle of rotation when configured with a Gyro or Inertial Sensor.
            drivetrain.rotation(DEGREES)

        When configured with a Gyro Sensor, the Drivetrain's Drive Rotation command reports
        an increasingly positive value when the Drivetrain turns in the counter-clockwise direction.

        Conversely, when configured with an Inertial Sensor, Drive Rotation reports
        an increasingly positive value when the Drivetrain turns in the clockwise direction.
    """)
    @sense
    def rotation(self, units: RotationUnits = RotationUnits.DEG) -> float:
        """Reports the Drivetrain's angle of rotation when configured with a Gyro or Inertial Sensor."""

    @robotmesh_doc("""
        Get the average current velocity of all motors.

        Returns:
        a float that represents the average current velocity

        Parameters:
        - velocityUnits: The measurement unit for the velocity.
    """)
    @vexcode_doc("""
        Reports the current velocity of the Drivetrain.
            drivetrain.velocity(UNITS)

        Drive Velocity returns a decimal value representing the current velocity of the Drivetrain.
        Acceptable UNITS are PERCENT and RPM.
            - If the provided UNITS parameter is PERCENT, the reported values ranges between -100 to 100.
            - Alternatively, if the provided UNITS is RPM, the reported values range between -127 to 127.
    """)
    @sense
    def velocity(self, velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:   # noqa: E501
        """Return Motor Velocity."""

    @robotmesh_doc("""
        Get the electrical current of all motors.

        Returns:
        a float that represents the electrical current of the motor in Amps.
    """)
    @vexcode_doc("""
        Reports the amount of current that the Drivetrain is currently using.
            drivetrain.current(UNITS)
        Drive Current reports a range from 0.0 to 2.5 when CurrentUnits.AMP is passed as the UNITS parameter.
    """)
    @sense
    def current(self, units : ElectricCurrentUnits = ElectricCurrentUnits.AMP) -> float:
        """Return Motors' Electrical Current."""
