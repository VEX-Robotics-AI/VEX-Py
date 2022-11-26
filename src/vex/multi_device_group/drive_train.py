"""Drive Train."""


from collections.abc import Sequence
from typing import Literal, Optional
from typing_extensions import Self

from abm.decor import act, sense

from ..motor import Motor
from ..motor.brake_type import BrakeType, BRAKE
from ..motor.current_units import CurrentUnits
from ..motor.direction_type import DirectionType, FORWARD
from ..motor.turn_type import TurnType, RIGHT
from ..motor.velocity_units import VelocityUnits, PERCENT
from ..time.time_units import SECONDS
from .._common_enums.distance import DistanceUnits, MM
from .._common_enums.numeric import NumType
from .._common_enums.rotation import DEGREES

from .._util.doc import vexcode_doc

from .motor_group import MotorGroup


__all__: Sequence[str] = ('DriveTrain',)


class DriveTrain(MotorGroup):  # pylint: disable=too-many-instance-attributes
    """Drive Train."""

    def __init__(self, left_motor: Motor, right_motor: Motor,
                 wheel_base: float = 200, track_width: float = 176,
                 length_unit: DistanceUnits = MM, gear_ratio: float = 1, /):
        """Initialize Drivetrain."""
        super().__init__(left_motor, right_motor)

        self.left_motor: Motor = left_motor
        self.right_motor: Motor = right_motor
        self.wheel_base: float = wheel_base
        self.track_width: float = track_width
        self.length_unit: DistanceUnits = length_unit
        self.gear_ratio: float = gear_ratio

        self.drive_velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.turn_velocities: dict[VelocityUnits, float] = \
            dict[VelocityUnits, float]()
        self.stopping_mode: Optional[BrakeType] = None
        self.timeout: Optional[float] = None

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, DriveTrain) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.wheel_base == self.wheel_base) and
                (other.track_width == self.track_width) and
                (other.length_unit == self.length_unit) and
                (other.gear_ratio == self.gear_ratio))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.left_motor, self.right_motor,
                     self.wheel_base, self.track_width,
                     self.length_unit, self.gear_ratio))

    @vexcode_doc("""
        Drive

        Moves the Drivetrain forever in the direction
        specified inside the parentheses.

        All Drivetrain motors run forward or in reverse
        at the velocity set using the Drivetrain's Set Drive Velocity command.
        The default velocity is 50%.

        Negative values will cause the Drivetrain to
        drive forward with a REVERSE input and in reverse with a FORWARD input.

        The Drive command will run the Drivetrain forever,
        until a new drivetrain command is used, or the program is stopped.
    """)
    @act
    def drive(self, direction: DirectionType = FORWARD):
        """Drive in specified direction."""

    @vexcode_doc("""
        Drive For

        Moves the Drivetrain for a given distance.
        All Drivetrain motors run forward or in reverse at the velocity
        set by the Drivetrain's Set Drive Velocity command.
        After the Drivetrain has moved the specified distance
        the Drivetrain will stop.

        Set how far the Drivetrain will move by entering at least
        three valid arguments inside of the parentheses, separated by commas.

        - The first argument specifies the direction.
          Valid inputs are either FORWARD or REVERSE in all capital letters.

        - The second argument specifies the distance
          that the IQ Robot should drive.

        - The third argument specifies the unit of measurement
          that should be used. Valid inputs are either INCHES or MM
          (millimeters) in all-capital letters.

        The DISTANCE parameter accepts numeric values.
        Negative values will cause the IQ Robot to drive
        in the opposite of the input DIRECTION.

        The Drive For command is by default a blocking command.
        It will prevent subsequent commands from executing
        until the Drivetrain movement has completed.

        You can set a fourth parameter to wait=False to allow
        proceeding commands to run even before the Drivetrain is done moving.
    """)
    @act
    def drive_for(self, direction: DirectionType = FORWARD,
                  distance: NumType = 200, units: DistanceUnits = MM,
                  wait: bool = True):
        """Drive for a distance."""

    @vexcode_doc("""
        Turn

        Turns the Drivetrain to the right or left indefinitely.

        The Turn command will rotate the Drivetrain in the given direction
        forever until a new Drivetrain command is used,
        or until the program is stopped.

        Use the LEFT argument in all-capital letters
        to turn the Drivetrain to the left.

        Use the RIGHT argument in all-capital letters
        to turn the Drivetrain to the right.
    """)
    @act
    def turn(self, direction: TurnType = RIGHT):
        """Turn in specified direction."""

    @vexcode_doc("""
        Turn For

        Turns the Drivetrain in the specified direction
        for a set number of degrees.

        - The first argument specifies the turn direction: LEFT or RIGHT,
          written in all-capital letters.

        - The second argument specifies the turn angle as a numeric value;
          this can be any number or numeric variable.

        - The third argument is the turn unit.
          This should be set as DEGREES in all-capital letters.

        The Turn For command is by default a blocking command.
        It prevents any proceeding code from executing until
        the Drivetrain has completed its turn.

        If the fourth argument is set to wait=False,
        proceeding commands will be allowed to execute
        even before the Drivetrain has completed its turn.
    """)
    @act
    def turn_for(self, direction: TurnType = RIGHT,
                 angle: NumType = 90, units: Literal[DEGREES] = DEGREES,
                 wait: bool = True):
        # pylint: disable=unused-argument
        """Turn for an angle."""
        assert units is DEGREES, ValueError('*** ANGULAR UNIT MUST BE DEGREES ***')  # noqa: E501

    @vexcode_doc("""
        Stop

        Stops the Drivetrain.

        The Stop command stops the Drivetrain.
        It does not take any arguments in its parentheses.
    """)
    @act
    def stop(self):
        """Stop motors."""

    @vexcode_doc("""
        Set Drive Velocity

        Sets the velocity of the Drivetrain for Drive and Drive For commands.

        Set Drive Velocity will set the Drivetrain's velocity
        when used with a Drive or Drive For command.
        It will not cause the Drivetrain to move when used by itself.

        Set Drive Velocity accepts a range of values
        depending on what units are passed as the second parameter.

        If PERCENT is used as the second parameter,
        VELOCITY accepts a range from -100 to 100.

        Set Drive Velocity can also use RPM as a valid UNITS parameter,
        accepting a range from -127 to 127.

        Setting a Drivetrain's drive velocity to a negative value
        will cause the Drivetrain to drive opposite of the DIRECTION
        passed into a Drive or Drive For command.

        Setting a Drivetrain's drive velocity to 0 will prevent the Drivetrain
        from moving even if a Drive or Drive For command is used.
    """)
    @act
    def set_drive_velocity(self, velocity: NumType = 50,
                           units: VelocityUnits = PERCENT):
        """Set driving velocity."""
        self.drive_velocities[units] = velocity

    @vexcode_doc("""
        Set Turn Velocity

        Sets the Drivetrain's turn velocity.

        Set Turn Velocity will set the velocity of the Drivetrain when turning,
        but will not cause the Drivetrain to move
        when used without a Turn or Turn For command.

        Set Turn Velocity accepts a range of values
        depending on what units are passed as the second parameter.

        If PERCENT is used as the second parameter,
        VELOCITY accepts a range from -100 to 100.

        Alternatively, Set Turn Velocity can also use RPM as a valid UNITS
        parameter, accepting a range from -127 to 127 as the VELOCITY.

        Setting a Drivetrain's turn velocity to a negative value
        will cause the Drivetrain to turn in the opposite of the direction
        passed into any following drivtrain.turn commands.

        Setting a Drivetrain's turn velocity to 0
        will prevent the Drivetrain from turning.
    """)
    @act
    def set_turn_velocity(self, velocity: NumType = 50,
                          units: VelocityUnits = PERCENT):
        """Set turning velocity."""
        self.turn_velocities[units] = velocity

    @vexcode_doc("""
        Set Motor Stopping

        Sets the behavior of an IQ Motor or Motor Group once it stops moving.

        The MODE parameter can be replaced with any of the following options:
        - BRAKE: will cause the Motor/Motor Group to come to an immediate stop.
        - COAST: lets the Motor/Motor Group spin gradually to a stop.
        - HOLD: will cause the Motor/Motor Group to come to an immediate stop,
                and returns it to its stopped position if moved.

        The stopping behavior set by this command
        will apply to subsequent Motor/Motor Group Stop commands
        for the entirety of the project, unless otherwise changed.
    """)
    @act
    def set_stopping(self, mode: BrakeType = BRAKE):
        # pylint: disable=arguments-differ
        """Set stopping mode."""
        self.stopping_mode: BrakeType = mode

    @vexcode_doc("""
        Set Timeout

        Sets a time limit for the Drivetrain's definite movement commands.

        The command is used to prevent definite movement commands
        that do not reach their position
        from preventing other proceeding commands from running.

        Specify the amount of time in SECONDS.
    """)
    @act
    def set_timeout(self, time: NumType = 1, /, units: Literal[SECONDS] = SECONDS):  # noqa: E501
        # pylint: disable=unused-argument
        """Set timeout."""
        self.timeout: float = time

    @vexcode_doc("""
        Drive Is Moving

        Reports if the Drivetrain is currently moving.

        Drive Is Moving reports True when the Drivetrain's motors are moving.
        Drive Is Moving reports False when the Drivetrain's motors are stopped.

        Note: This command will always return false if the Drivetrain is moving
        because of a drivetrain.drive or drivetrain.turn command
        (which do not specify a set distance to drive).
    """)
    @sense
    def is_moving(self) -> bool:
        """Report if drivetrain is still moving."""

    @vexcode_doc("""
        Drive Is Done

        Reports if the Drivetrain has completed its movement.

        Drive Is Done reports True
        when the robot's Drivetrain has completed its movement.

        Drive Is Done reports False
        when the robot's Drivetrain is still moving.
    """)
    @sense
    def is_done(self) -> bool:
        """Check whether drivetrain has finished driving/turning."""

    @vexcode_doc("""
        Drive Velocity

        Reports the current velocity of the Drivetrain.

        Drive Velocity returns a decimal value
        representing the current velocity of the Drivetrain.

        Acceptable UNITS are PERCENT and RPM.

        - If the provided UNITS parameter is PERCENT,
          the reported values ranges between -100 to 100.

        - Alternatively, if the provided UNITS is RPM,
          the reported values range between -127 to 127.
    """)
    @sense
    def velocity(self, units: VelocityUnits = PERCENT) -> float:
        # pylint: disable=arguments-differ
        """Return velocity."""

    @vexcode_doc("""
        Drive Current

        Reports the amount of current that the Drivetrain is currently using.

        Drive Current reports a range from 0.0 to 2.5
        when CurrentUnits.AMP is passed as the UNITS parameter.
    """)
    @sense
    def current(self, units: Literal[CurrentUnits.AMP] = CurrentUnits.AMP) -> float:  # noqa: E501
        # pylint: disable=arguments-differ
        """Return electrical current."""
