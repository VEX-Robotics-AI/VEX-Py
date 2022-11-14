"""Brain-built-in Inertial Sensor."""


from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

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


def _check_rotation_unit(rotation_unit: RotationUnits, /):
    assert rotation_unit is DEGREES, ValueError('*** ROTATION UNIT MUST BE '
                                                'DEGREES ***')


class Inertial(SingletonDevice):
    """Brain-built-in Inertial Sensor."""

    def __init__(self):
        """Initialize Brain-built-in Inertial Sensor."""

    @vexcode_doc("""
        Calibrates a VEX IQ (2nd generation) Brain's Inertial Sensor to reduce the amount of drift generated.
            brain_inertial.calibrate()

        Drifting occurs when the IQ (2nd generation) Brain's Inertial Sensor incorrectly detects movement
        even though the sensor is not physically moving.

        The IQ (2nd generation) Brain's Inertial Sensor must remain still during the calibration process.
        The calibration process will take approximately 2 seconds to complete.
    """)
    @act
    def calibrate(self):
        """Calibrates a VEX IQ (2nd generation) Brain's Inertial Sensor to reduce the amount of drift generated."""

    @vexcode_doc("""
        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading position to a specified heading.
            brain_inertial.set_heading(HEADING, DEGREES)

        Inertial Set Heading can be used to set the IQ (2nd generation) Brain's Inertial Sensor's position
        to any clockwise-positive heading. This command is typically used to reset the orientation of the
        IQ (2nd generation) Brain Inertial Sensor when the heading is set to a value of 0.
        Inertial Set Heading accepts a range of 0.0 to 359.99 for the HEADING parameter.
    """)
    @act
    def set_heading(self, heading: float = 0, rotation_unit: RotationUnits = DEGREES):
        """Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's current heading position to a specified heading."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc("""
        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's angle of rotation to a specified rotation.
            brain_inertial.set_rotation(ROTATION, DEGREES)

        The Inertial Set Rotation command can be used to set the IQ (2nd generation) Brain's Inertial Sensor's
        angle of rotation to any given positive (clockwise) or negative (counter-clockwise) value.
    """)
    @act
    def set_rotation(self, rotation: float = 0, rotation_unit: RotationUnits = DEGREES):
        """Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's angle of rotation to a specified rotation."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc("""
        Inertial Heading

        Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's
        current heading in degrees.

        The Inertial Heading command reports an increase in heading
        when rotating clockwise.

        Inertial Heading reports a range of values from 0.00 to 359.99 degrees.
    """)
    @sense
    def heading(self, rotation_unit: Literal[DEGREES] = DEGREES, /) -> float:
        """Return current heading in degrees."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc("""
        Inertial Rotation

        Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's
        current angle of rotation in degrees.

        The Inertial Rotation command reports an increasingly positive value
        when the Inertial Sensor turns in the clockwise direction.

        Inertial Rotation reports an increasingly negative value
        when the Inertial Sensor turns in the counter-clockwise direction.
    """)
    @sense
    def rotation(self, rotation_unit: Literal[DEGREES] = DEGREES, /) -> float:
        """Return current angle of rotation in degrees."""
        _check_rotation_unit(rotation_unit)

    @vexcode_doc("""
        Inertial Acceleration

        Reports the acceleration value from one of the axes (x, y, or z)
        on the VEX IQ (2nd generation) Brain's Inertial Sensor.

        Replace the AXIS parameter with one of the following options
        to get the acceleration values along the selected axis:
        - AxisType.XAXIS:
            reports acceleration of an Inertial Sensor's forward-to-backward
            movements
        - AxisType.YAXIS:
            reports acceleration of an Inertial Sensor's side-to-side movements
        - AxisType.ZAXIS:
            reports acceleration of an Inertial Sensor's up-to-down movements

        Inertial Acceleration returns a decimal value that ranges
        from -4.0 to 4.0 Gs.
    """)
    @sense
    def acceleration(self, axis_type: AxisType, /) -> float:
        """Return acceleration in one of the axes (x, y, or z)."""

    @vexcode_doc("""
        Inertial Gyro Rate

        Gets the rate of rotation for the specified axis (x, y, or z)
        on a VEX IQ (2nd generation) Brain's Inertial Sensor.

        Replace the AXIS parameter with one of the following options
        to get the gyro rate along an axis on the Inertial Sensor:
        - AxisType.XAXIS:
            reports rotation when the Inertial Sensor rotates in the X-Axis
            (based on the orientation of the sensor)
        - AxisType.YAXIS:
            reports rotation when the Inertial Sensor rotates in the Y-Axis
            (based on the orientation of the sensor)
        - AxisType.ZAXIS:
            reports rotations when the Inertial Sensor rotates in the Z-Axis
            (based on the orientation of the sensor)

        Inertial Gyro Rate is used to return a range from -1000.0 to 1000.0
        in dps (degrees per second)
    """)
    @sense
    def gyro_rate(
            self, axis_type: AxisType,
            velocity_unit: Literal[VelocityUnits.DPS] = VelocityUnits.DPS, /) \
            -> float:
        # pylint: disable=unused-argument
        """Return rate of rotation for specified axis (x, y, or z)."""
        assert velocity_unit is VelocityUnits.DPS, \
            ValueError('*** VELOCITY UNIT MUST BE DPS ***')

    @vexcode_doc("""
        Inertial Orientation

        Gets an orientation angle
        of the VEX IQ (2nd generation) Brain's Inertial Sensor.

        The orientation reported is determined by the selected axis
        (x, y, or z).

        Replace the TYPE parameter with one of the following options:
        - OrientationType.PITCH:
            represents pitch, which reports a value between -90 to +90 degrees
        - OrientationType.ROLL:
            represents roll, which reports a value between -180 to +180 degrees
        - OrientationType.YAW:
            represents yaw, which reports a value between -180 to +180 degrees
    """)
    @sense
    def orientation(self, orientation_type: OrientationType,
                    rotation_unit: Literal[DEGREES] = DEGREES, /) -> int:
        # pylint: disable=unused-argument
        """Return orientation angle."""
        _check_rotation_unit(rotation_unit)
