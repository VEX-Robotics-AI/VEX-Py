"""Distance Sensor."""


from collections.abc import Sequence

from abm.decor import sense

from .._abstract_device import Device
from ..brain.port import Ports
from .._common_enums.distance import DistanceUnits, MM, INCHES

from .._util.doc import vexcode_doc

from .object_size_type import ObjectSizeType
from .sonar import Sonar


__all__: Sequence[str] = 'Distance', 'ObjectSizeType', 'Sonar'


class Distance(Device):
    """Distance Sensor."""

    def __init__(self, port: Ports, /):
        """Initialize Distance Sensor."""
        self.port: Ports = port

    def __hash__(self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @vexcode_doc("""
        Distance Object Detected

        Reports if a VEX IQ Distance Sensor (2nd generation)
        detects an object or surface in its range.

        Distance Object Detected returns True if an object or surface
        is detected in its range, and False if not.
    """)
    @sense
    def is_object_detected(self) -> bool:
        """Check if an object is detected within range."""

    @vexcode_doc("""
        Distance Object Distance

        Reports the distance of the nearest object or surface
        from a VEX IQ Distance Sensor (2nd generation).

        Distance Object Distance accepts MM or INCHES as the UNITS parameter
        and reports a range from 20 to 2000 mm (millimeters)
        or approximately 0.8 to 79.0 inches.
    """)
    @sense
    def object_distance(self, unit: DistanceUnits = MM, /) -> int:
        """Return measured distance to nearby object."""
        assert unit in (MM, INCHES), ValueError('*** UNIT MUST BE MM OR INCHES ***')  # noqa: E501

    @vexcode_doc("""
        Distance Object Velocity

        Reports the velocity of a detected object in m/s.

        Distance Object Velocity reports
        the current velocity of an object in m/s (meters per second).

        The velocity of a detected object will change when the object is moving
        while in the range of an IQ Distance Sensor (2nd generation).
    """)
    @sense
    def object_velocity(self) -> float:
        """Return velocity of detected object in m/s."""

    @vexcode_doc("""
        Distance Object Size

        Reports an estimation of the detected object's size.

        Distance Object Size can be used to approximately determine
        if a detected object is of a certain size.

        There are three defined sizes that can be used for comparison:
            ObjectSizeType.SMALL
            ObjectSizeType.MEDIUM
            ObjectSizeType.LARGE
    """)
    @sense
    def object_size(self) -> ObjectSizeType:
        """Return an estimation of the detected object's size."""
