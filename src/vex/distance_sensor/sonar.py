"""Sonar."""


from collections.abc import Sequence
from typing import LiteralString, Self, overload

from abm.decor import act, sense

from .._device import Device
from ..brain.port import Ports
from .._common_enums.distance import DistanceUnits, MM, INCHES

from .._util.doc import robotmesh_doc, vexcode_doc
from .._util.type import Num


__all__: Sequence[LiteralString] = ('Sonar',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_sonar.html
""")
class Sonar(Device):
    """Sonar."""

    @robotmesh_doc("""
        Creates new sonar sensor object on the port specified in the parameter.

        Parameters
        - index: to the brain port.
    """)
    def __init__(self: Self, index: Ports, /):
        """Initialize Sonar."""
        self.port: Ports = index

        self.max_distance: dict[DistanceUnits, Num] = \
            dict[DistanceUnits, Num]()

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Sets the maximum distance (default 2.5m).

        Parameters
        - distance: maximum distance to be measured in units
        - distanceUnits: a DistanceUnits enum value for the measurement unit
    """)
    @act
    def set_maximum(self: Self,
                    distance: Num, distanceUnits: DistanceUnits = MM, /):
        """Set maximum measurable distance."""
        self.max_distance[distanceUnits] = distance

    @vexcode_doc("""
        Distance Found Object

        Reports if a VEX IQ Distance Sensor (1st generation)
        detects an object within its field of view.

        Reports True when a Distance Sensor detects an object or surface
        within its field of view.

        Reports False when a Distance Sensor does not detect an object
        or surface.
    """)
    @sense
    def is_object_detected(self: Self) -> bool:
        """Check if an object is detected within range."""

    @overload
    def distance(self: Self, unit: DistanceUnits = MM, /) -> int:
        ...

    @overload
    def distance(self: Self, distanceUnits: DistanceUnits = MM, /) -> int:
        ...

    @robotmesh_doc("""
        Gets the value of the sonar sensor.

        Parameters
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns
        an integer that represents the unit value specified by the parameter.
    """)
    @vexcode_doc("""
        Distance From

        Reports the distance of the nearest object
        from a VEX IQ Distance Sensor (1st generation).

        Distance From reports a range of values
        between 24 to 1000 mm (millimeters) or 1 to 40 in (inches).

        Specify whether the value returned by Distance From is reported
        in inches or mm (millimeters) by replacing the UNITS parameter
        with either INCHES or MM, respectively.
    """)
    @sense
    def distance(self: Self, unit: DistanceUnits = MM, /) -> int:
        """Return measured distance to nearby object."""
        assert unit in (MM, INCHES), ValueError('*** UNIT MUST BE MM OR INCHES ***')  # noqa: E501
