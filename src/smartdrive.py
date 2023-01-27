"""VEX Smart Drivetrain.

Robot Mesh VEX IQ Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacesmartdrive.html

Robot Mesh VEX V5 Python:
robotmesh.com/studio/content/docs/vexv5-python/html/namespacesmartdrive.html
"""


from collections.abc import Sequence
from typing import LiteralString, Optional, Self

from abm.decor import act, sense

from vex.motor.velocity import VelocityUnits
from vex.gyro_sensor import Gyro
from vex._common_enums.distance import DistanceUnits
from vex._common_enums.rotation import RotationUnits

from vex._util.doc import robotmesh_doc
from vex._util.type import NumType

from drivetrain import Drivetrain, DrivetrainMotorType


__all__: Sequence[LiteralString] = ('Smartdrive',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classsmartdrive_1_1_smartdrive.html
""")
class Smartdrive(Drivetrain):
    """VEX Smart Drivetrain."""

    @robotmesh_doc("""
        Create a new smartdrive object.

        Parameters
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
    """)
    def __init__(
            self,
            left_motor: DrivetrainMotorType, right_motor: DrivetrainMotorType,
            gyro: Gyro,
            wheel_travel: NumType = 200, track_width: NumType = 176,
            distanceUnits: DistanceUnits = DistanceUnits.MM,
            gear_ratio: NumType = 1, /):
        """Initialize Smart Drivetrain."""
        super().__init__(left_motor, right_motor,
                         wheel_travel, track_width, distanceUnits,
                         gear_ratio)

        self.gyro: Gyro = gyro

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, Smartdrive) and
                (other.left_motor == self.left_motor) and
                (other.right_motor == self.right_motor) and
                (other.gyro == self.gyro) and
                (other.wheel_travel == self.wheel_travel) and
                (other.track_width == self.track_width) and
                (other.distance_unit == self.distance_unit) and
                (other.gear_ratio == self.gear_ratio))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.left_motor, self.right_motor,
                     self.gyro,
                     self.wheel_travel, self.track_width,
                     self.distance_unit, self.gear_ratio))

    @robotmesh_doc("""
        Turn on the motors and rotate to a heading at the default velocity.

        Returns:
        True if the motor has reached the target rotation value.

        Parameters
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
    """)
    @act
    def turn_to_heading(
            self,
            angle: NumType, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[NumType] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Turn to specified heading angle."""

    @robotmesh_doc("""
        Turn to rotation.
    """)
    @act
    def turn_to_rotation(
            self,
            angle: NumType, angleUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[NumType] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Turn to specified rotational angle."""

    @robotmesh_doc("""
        Start turn to heading.
    """)
    @act
    def start_turn_to_heading(self,
                              angle: NumType,
                              angleUnits: RotationUnits = RotationUnits.DEG,
                              velocity: Optional[NumType] = None,
                              velocityUnits: VelocityUnits = VelocityUnits.PCT, /):  # noqa: E501
        """Start turning to specified target heading angle."""

    @robotmesh_doc("""
        Start turn to rotation.
    """)
    @act
    def start_turn_to_rotation(self,
                               angle: NumType,
                               angleUnits: RotationUnits = RotationUnits.DEG,
                               velocity: Optional[NumType] = None,
                               velocityUnits: VelocityUnits = VelocityUnits.PCT, /):  # noqa: E501
        """Start turning to specified target rotational angle."""

    @robotmesh_doc("""
        Check if turnToHeading, turnToRotation or turnFor is still running.

        Returns:
        True if the motor is on and is rotating to a target, False otherwise.

        Reimplemented from drivetrain.Drivetrain.
    """)
    @sense
    def is_done(self) -> bool:
        """Check if drivetrain has finished moving."""

    @property
    def gyro(self) -> Gyro:
        """Get Gyro Sensor."""
        return self._gyro

    @gyro.setter
    def gyro(self, gyro: Gyro):
        self._gyro: Gyro = gyro
