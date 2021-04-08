from enum import IntEnum

from __decor import act, sense

from .abstract import Device
from .port import Ports

class Gyro(Device):
    def __init__(self, index: Ports, calibrate=True):
        """
        Creates a new gyro object on the port specified in the parameter.

        params:
        index: index to the brain port.
        calibrate: set to calibrate the sensor now
        """

    def start_calibration(
        self,
        gyroCalibrationType=GyroCalibrationType.QUICK,
        waitForCompletion=True
    ):
        """
        Starts recalibration of the gyro.

        params:
        gyroCalibrationType: amount of time for calibration, GyroCalibrationType enum value.
        waitForCompletion: wait for calibration to complete
        """

    def is_calibrating(self):
        """
        Returns True while the gyro sensor is performing a requested recalibration, changing to false once recalibration has completed.

        Returns True if gyro is still calibrating.
        """

    def set_heading(self, value=0, rotationUnits=RotationUnits.DEG):
        """
        Set the gyro sensor angle to angle.

        params:
        value: The new heading for the gyro
        rotationUnits: The rotation unit for the heading
        """

    def set_rotation(self, value=0, rotationUnits=RotationUnits.DEG):
        """
        Set the gyro sensor rotation to angle.

        params:
        value: The new absolute angle for the gyro
        rotationUnits: The rotation unit for the angle
        """

    def heading(self, rotationUnits=RotationUnits.DEG):
        """
        Gets the angle of the gyro sensor.

        params:
        rotationUnits: The measurement unit for the gyro device.
        """

    def rotation(self, rotationUnits=RotationUnits.DEG):
        """
        Gets the absolute angle of the gyro sensor.

        params:
        rotationUnits: The measurement unit for the gyro device.
        """

class GyroCalibrationType(IntEnum):
    QUICK: int = 0
    SLOW: int = 1
    ACCURATE: int = 2
