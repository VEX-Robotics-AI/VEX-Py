"""VEX Brain."""


from __future__ import annotations

from collections.abc import Sequence

from abm.decor import act, sense

from ..._abstract_device import SingletonDevice
from ...motor import VelocityUnits
from ...units_common import RotationUnits, DEGREES
from ...util.doc import vexcode_doc

from .axis_type import AxisType, XAXIS, YAXIS, ZAXIS
from .orientation_type import OrientationType, PITCH, ROLL, YAW


__all__: Sequence[str] = ('Inertial',
                          'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
                          'OrientationType', 'PITCH', 'ROLL', 'YAW')


def _check_rotation_unit(rotation_unit: RotationUnits):
    if rotation_unit != DEGREES:
        raise ValueError("Incorrect rotation unit. Only accepts DEGREES.")


@vexcode_doc("""
    VEX IQ (2nd generation) Brain's Inertial Sensor.
""")
class Inertial(SingletonDevice):
    """VEX IQ (2nd generation) Brain's Inertial Sensor."""

    def __init__(self):
        """Initialize Brain's Inertial Sensor."""
        pass

    @vexcode_doc(
        """
        Calibrates a VEX IQ (2nd generation) Brain's Inertial Sensor to reduce the amount of drift generated.
            brain_inertial.calibrate()

        Drifting occurs when the IQ (2nd generation) Brain's Inertial Sensor incorrectly detects movement
        even though the sensor is not physically moving.

        The IQ (2nd generation) Brain's Inertial Sensor must remain still during the calibration process.
        The calibration process will take approximately 2 seconds to complete.
        """
    )
    @act
    def calibrate(self):
        """Calibrates a VEX IQ (2nd generation) Brain's Inertial Sensor to reduce the amount of drift generated."""

    @vexcode_doc(
        """
        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading position to a specified heading.
            brain_inertial.set_heading(HEADING, DEGREES)

        Inertial Set Heading can be used to set the IQ (2nd generation) Brain's Inertial Sensor's position
        to any clockwise-positive heading. This command is typically used to reset the orientation of the
        IQ (2nd generation) Brain Inertial Sensor when the heading is set to a value of 0.
        Inertial Set Heading accepts a range of 0.0 to 359.99 for the HEADING parameter.
        """
    )
    @act
    def set_heading(self, heading: float = 0, rotation_unit: RotationUnits = DEGREES):
        """Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading position to a specified heading."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc(
        """
        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's angle of rotation to a specified rotation.
            brain_inertial.set_rotation(ROTATION, DEGREES)

        The Inertial Set Rotation command can be used to set the IQ (2nd generation) Brain's Inertial Sensor's
        angle of rotation to any given positive (clockwise) or negative (counter-clockwise) value.
        """
    )
    @act
    def set_rotation(self, rotation: float = 0, rotation_unit: RotationUnits = DEGREES):
        """Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's angle of rotation to a specified rotation."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc(
        """
        Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading in degrees.
            brain_inertial.heading(DEGREES)

        The Inertial Heading command reports an increase in heading when rotating clockwise.
        Inertial Heading reports a range of values from 0.00 to 359.99 degrees.

        Example: turning a Drivetrain until the Inertial Sensor's heading value is more than 180 degrees before stopping
            drivetrain.turn(RIGHT)
            while not brain_inertial.heading(DEGREES) > 180:
                wait(0.1, SECONDS)
            drivetrain.stop()
        """
    )
    @sense
    def heading(self, rotation_unit: RotationUnits = DEGREES):
        """Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading in degrees."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc(
        """
        Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's current angle of rotation in degrees.
            brain_inertial.rotation(DEGREES)

        The Inertial Rotation command reports an increasingly positive value when the Inertial Sensor turns in the
        clockwise direction.
        Inertial Rotation reports an increasingly negative value when the Inertial Sensor turns in the
        counter-clockwise direction.

        Example: turning a Drivetrain until the Inertial Sensor's rotation value is > 180 degrees before stopping:
            drivetrain.turn(RIGHT)
            while not brain_inertial.rotation(DEGREES) > 180:
                wait(0.1, SECONDS)
            drivetrain.stop()
        """
    )
    @sense
    def rotation(self, rotation_unit: RotationUnits = DEGREES):
        """Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's current angle of rotation in degrees."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc(
        """
        Reports the acceleration value from one of the axes (x, y, or z) on the VEX IQ (2nd generation) Brain's
        Inertial Sensor.
            brain_inertial.acceleration(AXIS)

        Replace the AXIS parameter with one of the following options to get the acceleration values along
        the selected axis:
        * AxisType.XAXIS: reports acceleration of an Inertial Sensor's forward to backward movements
        * AxisType.YAXIS: reports acceleration of an Inertial Sensor's side to side movements
        * AxisType.ZAXIS: reports acceleration of an Inertial Sensor's up to down movements
        * Inertial Acceleration returns a decimal value that ranges from -4.0 to 4.0 Gs.

        Example: prints an Inertial Sensor's acceleration values to the VEX IQ Brain in a loop:
        ```
            # Set a smaller font to ensure lines fit when printed
            brain.screen.set_font(FontType.MONO12)

            while True:
                brain.screen.clear_screen()
                brain.screen.set_cursor(1, 1)

                # X Axis
                brain.screen.print("X:", brain_inertial.acceleration(AxisType.XAXIS))
                brain.screen.next_row()

                # Y Axis
                brain.screen.print("Y:", brain_inertial.acceleration(AxisType.YAXIS))
                brain.screen.next_row()

                # Z Axis
                brain.screen.print("Z:", brain_inertial.acceleration(AxisType.ZAXIS))
                brain.screen.next_row()

                # Brief wait to prevent tearing when printing values
                wait(0.1, SECONDS)
        ```"""
    )
    @sense
    def acceleration(self, axis_type: AxisType = AxisType.XAXIS):
        """Reports the acceleration value from one of the axes (x, y, or z) on the VEX IQ (2nd generation) Brain's
        Inertial Sensor.
        """

    @vexcode_doc(
        """
        Gets the rate of rotation for the specified axis (x, y, or z) on a VEX IQ (2nd generation) Brain's
        Inertial Sensor.
            brain_inertial.gyro_rate(AXIS, VelocityUnits.DPS)

        Replace the AXIS parameter with one of the following options to get the gyro rate along an axis on the
        Inertial Sensor:
        * AxisType.XAXIS: reports rotation when the Inertial Sensor rotates in the X-Axis
            (based on the orientation of the sensor)
        * AxisType.YAXIS: reports rotation when the Inertial Sensor rotates in the Y-Axis
            (based on the orientation of the sensor)
        * AxisType.ZAXIS: reports rotations when the Inertial Sensor rotates in the Z-Axis
            (based on the orientation of the sensor)
        Inertial Gyro Rate is used to return a range from -1000.0 to 1000.0 in dps (degrees per second).
        """
    )
    @sense
    def gyro_rate(
        self,
        axis_type: AxisType = AxisType.XAXIS,
        velocity_unit: VelocityUnits = VelocityUnits.DPS,
    ):
        """Gets the rate of rotation for the specified axis (x, y, or z) on a VEX IQ (2nd generation) Brain's
        Inertial Sensor.
        """
        if velocity_unit != VelocityUnits.DPS:
            raise ValueError("Incorrect velocity unit. Only accepts DPS.")

    @vexcode_doc(
        """
        Gets an orientation angle of the VEX IQ (2nd generation) Brain's Inertial Sensor.
            brain_inertial.orientation(TYPE, DEGREES)

        The orientation reported is determined by the selected axis (x, y, or z).
        Replace the TYPE parameter with one of the following options:
        * OrientationType.PITCH: represents pitch, which reports a value between -90 to +90 degrees.
        * OrientationType.ROLL: represents roll, which reports a value between -180 to +180 degrees.
        * OrientationType.YAW: represents yaw, which reports a value between -180 to +180 degrees.
        """
    )
    @sense
    def orientation(
        self,
        orientation_type: OrientationType = OrientationType.ROLL,
        rotation_unit: RotationUnits = DEGREES,
    ):
        """Gets an orientation angle of the VEX IQ (2nd generation) Brain's Inertial Sensor."""
        _check_rotation_unit(rotation_unit)
