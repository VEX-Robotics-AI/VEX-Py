"""VEX Distance Sensor."""


from collections.abc import Sequence

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..units_common import DistanceUnits

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc  # noqa: F401
from .object_size_type import ObjectSizeType


__all__: Sequence[str] = ("Sonar",)


@robotmesh_doc(
    """
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_sonar.html
"""
)
class Sonar(Device):
    """Sonar (Distance Sensor)."""

    @robotmesh_doc(
        """
        Create new sonar sensor object on the port specified in the parameter.

        Parameters:
        - index: to the brain port.
    """
    )
    def __init__(self, index: Ports, /):
        """Initialize Distance Sensor."""
        self.port: Ports = index

        self.max_distances: dict[DistanceUnits, float] = dict[DistanceUnits, float]()

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash(self.port)

    @robotmesh_doc(
        """
        Set the maximum distance (default 2.5m).

        Parameters:
        - distance: maximum distance to be measured in units
        - distanceUnits: a DistanceUnits enum value for the measurement unit.
    """
    )
    @act
    def set_maximum(
        self, distance: float, distanceUnits: DistanceUnits = DistanceUnits.MM, /
    ):
        """Set maximum measurable distance."""
        self.max_distances[distanceUnits] = distance

    @robotmesh_doc(
        """
        Get the value of the sonar sensor.

        Parameters:
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
    """
    )
    @sense
    def distance(
        self, distanceUnits: DistanceUnits = DistanceUnits.MM, /
    ) -> int:  # noqa: E501
        """Return measured distance to nearby object."""

    @vexcode_doc(
        """
        Get the value of the sonar sensor.

        Parameters:
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
    """
    )
    @sense
    def object_distance(
        self, distanceUnits: DistanceUnits = DistanceUnits.MM, /
    ) -> int:  # noqa: E501
        """Return measured distance to nearby object."""

    @vexcode_doc(
        """
        Distance Object Velocity reports the current velocity of an object in m/s (meters per second).

        The velocity of a detected object will change when the object is moving
        while in the range of an IQ Distance Sensor (2nd generation).
            brain.screen.print("Velocity:", distance.object_velocity())
        """
    )
    @sense
    def object_velocity(self) -> float:
        """Reports the velocity of a detected object in m/s."""

    @vexcode_doc(
        """
        Distance Object Size can be used to approximately determine if a detected object is of a certain size.

        There are three defined sizes that can be used for comparison:
            ObjectSizeType.SMALL
            ObjectSizeType.MEDIUM
            ObjectSizeType.LARGE

        The example below prints "Large!" to a VEX IQ Brain's screen
        if a large object is detected by an IQ Distance Sensor (2nd generation):
            if distance.object_size() == ObjectSizeType.LARGE:
                brain.screen.print("Large!")
        """
    )
    @sense
    def object_size(self) -> ObjectSizeType:
        """Reports an estimation of the detected object's size."""

    @vexcode_doc(
        """
        Distance Object Detected returns True if an object or surface is detected in its range, and False if not.

        The example below prints "True" to a VEX IQ Brain's screen if an object or surface is detected by a Distance Sensor.
            if dstance.is_object_detected():
                brain.screen.print("True")
        """
    )
    @sense
    def is_object_detected(self) -> bool:
        """Reports if a VEX IQ Distance Sensor (2nd generation) detects an object or surface in its range."""
