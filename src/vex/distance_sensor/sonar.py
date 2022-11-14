"""Sonar."""


from collections.abc import Sequence

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..units_common import DistanceUnits

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = ('Sonar',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_sonar.html
""")
class Sonar(Device):
    """Sonar."""

    @robotmesh_doc("""
        Create new sonar sensor object on the port specified in the parameter.

        Parameters:
        - index: to the brain port.
    """)
    def __init__(self, index: Ports, /):
        """Initialize Sonar."""
        self.port: Ports = index

        self.max_distances: dict[DistanceUnits, float] = dict[DistanceUnits, float]()  # noqa: E501

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Set the maximum distance (default 2.5m).

        Parameters:
        - distance: maximum distance to be measured in units
        - distanceUnits: a DistanceUnits enum value for the measurement unit.
    """)
    @act
    def set_maximum(self, distance: float,
                    distanceUnits: DistanceUnits = DistanceUnits.MM, /):
        """Set maximum measurable distance."""
        self.max_distances[distanceUnits] = distance

    @robotmesh_doc("""
        Get the value of the sonar sensor.

        Parameters:
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
    """)
    @sense
    def distance(self, distanceUnits: DistanceUnits = DistanceUnits.MM, /) -> int:  # noqa: E501
        """Return measured distance to nearby object."""
