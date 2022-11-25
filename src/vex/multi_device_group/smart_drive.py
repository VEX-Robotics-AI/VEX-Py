"""Smart Drive Train."""


from collections.abc import Sequence
from typing import Literal
from typing_extensions import Self

from abm.decor import act, sense

from ..motor import Motor
from ..brain.inertial_sensor import Inertial
from ..gyro_sensor import Gyro
from .._common_enums.distance import MM
from .._common_enums.numeric import NumType
from .._common_enums.rotation import DEGREES

from .._util.doc import vexcode_doc

from .drive_train import DriveTrain


__all__: Sequence[str] = ('SmartDrive',)


class SmartDrive(DriveTrain):
    """Smart Drive Train."""

    def __init__(self, left_motor: Motor, right_motor: Motor,
                 gyro_sensor: Inertial | Gyro = Inertial(),
                 wheel_size: float = 200, /):
        """Initialize Smart Drive Train."""
        super().__init__(left_motor, right_motor,
                         None,  # wheel_base
                         None,  # track_width
                         MM,  # length_unit
                         1  # gear_ratio
                         )

        self.gyro_sensor: Inertial | Gyro = gyro_sensor

        self.wheel_size: float = wheel_size

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, DriveTrain) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.gyro_sensor == self.gyro_sensor) and
                (other.wheel_size == self.wheel_size))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.left_motor, self.right_motor,
                     self.gyro_sensor, self.wheel_size))

    @vexcode_doc("""
        Set Heading

        Sets the Drivetrain's Inertial or Gyro Sensor to the specified heading.

        The Drivetrain's Set Heading command can be used to set the
        Drivetrain's heading to a specified value. This command can be used to
        reset the orientation of the Drivetrain's Inertial or Gyro Sensor
        when the heading is set to a value of 0.

        Set Heading accepts a number value between 0 and 360 as first argument,
        and DEGREES written in all-capital letters as its second argument.
    """)
    @act
    def set_heading(self, value: NumType = 0, units: Literal[DEGREES] = DEGREES):  # noqa: E501
        """Set specified heading."""

    @vexcode_doc("""
        Set Rotation

        Sets the Drivetrain's Inertial or Gyro Sensor to a specified rotation.

        The Drivetrain's Set Rotation command can be used to set the
        Drivetrain's angle of rotation to any given positive or negative value.

        The ROTATION parameter can accept numeric values.
        The ROTATION parameter does not have a limit of 0-359 degrees.
    """)
    @act
    def set_rotation(self, value: NumType = 0, units: Literal[DEGREES] = DEGREES):  # noqa: E501
        """Set specified rotation."""

    @vexcode_doc("""
        Turn To Heading

        Turns a Drivetrain to a specific heading,
        when using a Gyro or Inertial Sensor.

        The Turn to Heading command can be used to turn the Drivetrain to any
        given clockwise or counter-clockwise positive heading, depending on
        whether a Gyro or Inertial Sensor is configured with the Drivetrain.

        Based on the current heading,
        Turn to Heading will determine the shortest direction to turn.

        The HEADING parameter accepts numeric values between 0.00 to 359.99.

        The second parameter should be set to DEGREES.

        (The direction descriptions below are based on a clockwise positive
        heading, with the IQ (2nd generation) Brain's Inertial Sensor
        configured with the Drivetrain)

        The Turn to Heading command will by default block proceeding commands
        until the Drivetrain turn has completed.

        You can set wait=False as a third parameter to prevent
        the Turn to Heading command from blocking proceeding commands
        from executing until the Drivetrain turn has completed.
    """)
    @act
    def turn_to_heading(self, heading: float = 90,
                        unit: Literal[DEGREES] = DEGREES, wait: bool = True, /):  # noqa: E501
        """Turn to specific heading."""

    @vexcode_doc("""
        Turn To Rotation

        Turns the Drivetrain to a specific angle of rotation
        when used with a Gyro or Inertial Sensor.

        The Turn to Rotation command can be used to turn the Drivetrain
        to an absolute rotation value.

        Depending on whether the Drivetrain is configured with a Gyro or
        Inertial Sensor, rotation values can either be counter-clockwise
        positive (Gyro), or clockwise positive (Inertial).

        Based on the current rotation of the Drivetrain, Turn to Rotation will
        determine which direction to turn.

        The ROTATION parameter can accept numeric values.

        Numeric values are not limited to the range of 0 - 359.99 degrees.
        Turns will be absolute and may cause the robot to rotate more than once
        if necessary.

        (Direction descriptions above are aligned with an IQ (2nd generation)
        Brain's Inertial Sensor being configured with the Drivetrain)

        The Turn to Rotation command will by default block proceeding commands
        until the Drivetrain turn has completed.

        You can set a third parameter to wait=False to prevent
        the Turn to Rotation command from blocking proceeding commands until
        the Drivetrain turn is completed.
    """)
    @act
    def turn_to_rotation(self, rotation: float = 90,
                         unit: Literal[DEGREES] = DEGREES, wait: bool = True, /):  # noqa: E501
        """Turn to specific angle of rotation."""

    @vexcode_doc("""
        Drive Heading

        Reports the direction that the Drivetrain is facing by using the
        Gyro or Inertial Sensor's current angular position.

        Drive heading reports a range from 0.00 to 359.99 degrees.

        When the Drivetrain is configured with a Gyro Sensor, the Drive Heading
        command reports an increase in heading when rotating counter-clockwise.

        Alternatively, if the Drivetrain is configured with the IQ
        (2nd generation) Brain's Inertial Sensor, the Drive Heading command
        reports an increase in heading when rotating clockwise.
    """)
    @sense
    def heading(self, units: Literal[DEGREES] = DEGREES) -> float:
        """Return heading angle."""

    @vexcode_doc("""
        Drive Rotation

        Reports the Drivetrain's angle of rotation
        when configured with a Gyro or Inertial Sensor.

        When configured with a Gyro Sensor, the Drivetrain's Drive Rotation
        command reports an increasingly positive value when the Drivetrain
        turns in the counter-clockwise direction.

        Conversely, when configured with an Inertial Sensor, Drive Rotation
        reports an increasingly positive value when the Drivetrain turns in the
        clockwise direction.
    """)
    @sense
    def rotation(self, units: Literal[DEGREES] = DEGREES) -> float:
        """Return cumulative rotational angle."""
