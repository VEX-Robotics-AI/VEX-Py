from __decor import act, sense

from .abstract import Device


class Sonar(Device):
    def __init__(self, index):
        """
        Creates a new sonar sensor object on the port specified in the parameter.

        Params:
        index: to the brain port.
        """

    @act
    def set_maximum(self, distance, distanceUnits=DistanceUnits.MM):
        """
        Sets the maximum distance (default 2.5m)

        Params:
        distance: maximum distance to be measured in units
        distanceUnits: a DistanceUnits enum value for the measurement unit.
        """"

    @property
    def distance(self, distanceUnits=DistanceUnits.MM):
        """
        Gets the value of the sonar sensor.

        Params:
        distanceUnits: The measurement unit for the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
        """"
