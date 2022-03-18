from enum import IntEnum

from __vex_decor import act, sense

from .abstract import Device
from .port import Ports
from .units_common import RotationUnits


class GyroCalibrationType(IntEnum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2


class Gyro(Device):
    def __init__(self, index: Ports, calibrate: bool = True):
        """
        Creates a new gyro object on the port specified in the parameter.

        Parameters:
        - index: index to the brain port.
        - calibrate: set to calibrate the sensor now
        """
        self.port: Ports = index
        self.calibrate: bool = calibrate

        self.headings: dict[RotationUnits, float] = \
            dict[RotationUnits, float]()
        self.rotations: dict[RotationUnits, float] = \
            dict[RotationUnits, float]()

    @act
    def start_calibration(
            self,
            gyroCalibrationType: GyroCalibrationType
            = GyroCalibrationType.QUICK,
            waitForCompletion: bool = True):
        """
        Starts recalibration of the gyro.

        Parameters:
        - gyroCalibrationType: amount of time for calibration,
                               GyroCalibrationType enum value.
        - waitForCompletion: wait for calibration to complete
        """

    @sense
    def is_calibrating(self) -> bool:
        """
        Returns True while the gyro sensor is performing
        a requested recalibration, changing to false
        once recalibration has completed.

        Returns True if gyro is still calibrating.
        """

    @act
    def set_heading(
            self,
            value: float = 0,
            rotationUnits: RotationUnits = RotationUnits.DEG):
        """
        Set the gyro sensor angle to angle.

        Parameters:
        - value: The new heading for the gyro
        - rotationUnits: The rotation unit for the heading
        """
        self.headings[rotationUnits] = value

    @act
    def set_rotation(
            self,
            value: float = 0,
            rotationUnits: RotationUnits = RotationUnits.DEG):
        """
        Set the gyro sensor rotation to angle.

        Parameters:
        - value: The new absolute angle for the gyro
        - rotationUnits: The rotation unit for the angle
        """
        self.rotations[rotationUnits] = value

    @sense
    def heading(
            self,
            rotationUnits: RotationUnits = RotationUnits.DEG) -> float:
        """
        Gets the angle of the gyro sensor.

        Parameters:
        - rotationUnits: The measurement unit for the gyro device.
        """

    @sense
    def rotation(
            self,
            rotationUnits: RotationUnits = RotationUnits.DEG) -> float:
        """
        Gets the absolute angle of the gyro sensor.

        Parameters:
        - rotationUnits: The measurement unit for the gyro device.
        """
