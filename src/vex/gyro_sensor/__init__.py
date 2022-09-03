"""VEX Gyro Sensor."""


from collections.abc import Sequence

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..units_common import RotationUnits

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from .calibration_type import GyroCalibrationType


__all__: Sequence[str] = 'Gyro', 'GyroCalibrationType'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_gyro.html
""")
class Gyro(Device):
    """Gyro Sensor."""

    @robotmesh_doc("""
        Create a new gyro object on the port specified in the parameter.

        Parameters:
        - index: index to the brain port.
        - calibrate: set to calibrate the sensor now
    """)
    def __init__(self, index: Ports, calibrate: bool = True, /):
        """Initialize Gyro Sensor."""
        self.port: Ports = index
        self.calibrate: bool = calibrate

        self.headings: dict[RotationUnits, float] = dict[RotationUnits, float]()   # noqa: E501
        self.rotations: dict[RotationUnits, float] = dict[RotationUnits, float]()   # noqa: E501

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash((self.port, self.calibrate))

    @robotmesh_doc("""
        Start recalibration of the gyro.

        Parameters:
        - gyroCalibrationType: amount of time for calibration,
                               GyroCalibrationType enum value.
        - waitForCompletion: wait for calibration to complete
    """)
    @act
    def start_calibration(
            self,
            gyroCalibrationType: GyroCalibrationType = GyroCalibrationType.QUICK,   # noqa: E501
            waitForCompletion: bool = True, /):
        """Start calibrating Gyro Sensor."""

    @robotmesh_doc("""
        Return True while  gyro sensor is performing a requested recalibration.

        (changing to false once recalibration has completed)

        Returns True if gyro is still calibrating.
    """)
    @sense
    def is_calibrating(self) -> bool:
        """Check if Gyro Sensor is calibrating."""

    @robotmesh_doc("""
        Set the gyro sensor angle to angle.

        Parameters:
        - value: The new heading for the gyro
        - rotationUnits: The rotation unit for the heading
    """)
    @act
    def set_heading(self, value: float = 0,
                    rotationUnits: RotationUnits = RotationUnits.DEG, /):
        """Set Gyro Heading Angle Value."""
        self.headings[rotationUnits] = value

    @robotmesh_doc("""
        Set the gyro sensor rotation to angle.

        Parameters:
        - value: The new absolute angle for the gyro
        - rotationUnits: The rotation unit for the angle
    """)
    @act
    def set_rotation(self, value: float = 0,
                     rotationUnits: RotationUnits = RotationUnits.DEG, /):
        """Set Gyro Cumulative Rotation Angle Value."""
        self.rotations[rotationUnits] = value

    @robotmesh_doc("""
        Get the angle of the gyro sensor.

        Parameters:
        - rotationUnits: The measurement unit for the gyro device.
    """)
    @sense
    def heading(self, rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:   # noqa: E501
        """Return Gyro Heading Angle Value."""

    @robotmesh_doc("""
        Get the absolute angle of the gyro sensor.

        Parameters:
        - rotationUnits: The measurement unit for the gyro device.
    """)
    @sense
    def rotation(self, rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:   # noqa: E501
        """Return Gyro Cumulative Rotation Angle Value."""
