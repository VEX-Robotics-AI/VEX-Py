"""Brain-built-in Inertial Sensor."""


from collections.abc import Sequence
from typing import Literal, LiteralString, Self

from abm.decor import act, sense

from ..._abstract_device import SingletonDevice
from ...motor import VelocityUnits
from ..._common_enums.axis import AxisType
from ..._common_enums.orientation import OrientationType
from ..._common_enums.rotation import RotationUnits, DEGREES

from ..._util.doc import vexcode_doc


__all__: Sequence[LiteralString] = ('Inertial',)


def _ensure_rotation_unit_is_degrees(unit: RotationUnits, /):
    assert unit is DEGREES, ValueError('*** ROTATION UNIT MUST BE DEGREES ***')


class Inertial(SingletonDevice):
    """Brain-built-in Inertial Sensor."""

    def __init__(self):
        """Initialize Brain-built-in Inertial Sensor."""

    @vexcode_doc("""
        Inertial Calibrate

        Calibrates a VEX IQ (2nd generation) Brain's Inertial Sensor
        to reduce the amount of drift generated.

        Drifting occurs when the IQ (2nd generation) Brain's Inertial Sensor
        incorrectly detects movement even though
        the sensor is not physically moving.

        The IQ (2nd generation) Brain's Inertial Sensor must remain still
        during the calibration process. The calibration process will take
        approximately 2 seconds to complete.
    """)
    @act
    def calibrate(self):
        """Calibrate."""

    @vexcode_doc("""
        Inertial Set Heading

        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's
        current heading position to a specified heading.

        Inertial Set Heading can be used
        to set the IQ (2nd generation) Brain's Inertial Sensor's position
        to any clockwise-positive heading. This command is typically used to
        reset the orientation of the IQ (2nd generation) Brain Inertial Sensor
        when the heading is set to a value of 0.

        Inertial Set Heading accepts a range of 0.0 to 359.99
        for the HEADING parameter.
    """)
    @act
    def set_heading(self: Self,
                    value: float = 0, unit: Literal[DEGREES] = DEGREES, /):
        # pylint: disable=unused-argument
        """Set heading to specified angle."""
        _ensure_rotation_unit_is_degrees(unit)

    @vexcode_doc("""
        Inertial Set Rotation

        Sets a VEX IQ (2nd generation) Brain's Inertial Sensor's
        angle of rotation to a specified rotation.

        The Inertial Set Rotation command can be used
        to set the IQ (2nd generation) Brain's Inertial Sensor's
        angle of rotation to any given positive (clockwise)
        or negative (counter-clockwise) value.
    """)
    @act
    def set_rotation(self: Self,
                     value: float = 0, unit: Literal[DEGREES] = DEGREES, /):
        # pylint: disable=unused-argument
        """Set rotational angle to specified value."""
        _ensure_rotation_unit_is_degrees(unit)

    @vexcode_doc("""
        Inertial Heading

        Reports a VEX IQ (2nd generation) Brain's Inertial Sensor's
        current heading in degrees.

        The Inertial Heading command reports an increase in heading
        when rotating clockwise.

        Inertial Heading reports a range of values from 0.00 to 359.99 degrees.
    """)
    @sense
    def heading(self: Self, unit: Literal[DEGREES] = DEGREES, /) -> float:
        """Return current heading in degrees."""
        _ensure_rotation_unit_is_degrees(unit)

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
    def rotation(self: Self, unit: Literal[DEGREES] = DEGREES, /) -> float:
        """Return current angle of rotation in degrees."""
        _ensure_rotation_unit_is_degrees(unit)

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
    def acceleration(self: Self, axis: AxisType = AxisType.XAXIS, /) -> float:
        """Return acceleration in Axis X, Y or Z."""

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
    def gyro_rate(self: Self, axis: AxisType = AxisType.XAXIS,
                  unit: Literal[VelocityUnits.DPS] = VelocityUnits.DPS, /) -> float:  # noqa: E501
        # pylint: disable=unused-argument
        """Return rate of rotation for Axis X, Y or Z."""
        assert unit is VelocityUnits.DPS, ValueError('*** UNIT MUST BE DPS ***')  # noqa: E501

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
    def orientation(self: Self, axis: OrientationType = OrientationType.ROLL,
                    unit: Literal[DEGREES] = DEGREES, /) -> float:
        # pylint: disable=unused-argument
        """Return orientation angle."""
        _ensure_rotation_unit_is_degrees(unit)
