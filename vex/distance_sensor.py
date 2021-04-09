from __decor import act, sense

from .abstract import Device
from .port import Ports


class Sonar(Device):
    def __init__(self, index: Ports):
        """
        Creates a new sonar sensor object on
        the port specified in the parameter.

        Parameters:
        - index: to the brain port.
        """
        pass

    @act
    def set_maximum(
            self,
            distance: float,
            distanceUnits: DistanceUnits = DistanceUnits.MM):
        """
        Sets the maximum distance (default 2.5m)

        Parameters:
        - distance: maximum distance to be measured in units
        - distanceUnits: a DistanceUnits enum value for the measurement unit.
        """"
        pass

    @sense
    def distance(
            self,
            distanceUnits: DistanceUnits = DistanceUnits.MM) -> int:
        """
        Gets the value of the sonar sensor.

        Parameters:
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
        """"
