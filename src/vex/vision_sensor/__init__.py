"""Vision Sensor."""


from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self

from abm.decor import sense

from .._abstract_device import Device
from ..brain.port import Ports

from .._util.doc import robotmesh_doc, vexcode_doc

from .vision_object import VisionObject


__all__: Sequence[str] = 'Vision', 'VisionObject'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvision_1_1_vision.html
""")
class Vision(Device):
    """Vision Sensor."""

    @robotmesh_doc("""
        Creates a new vision object on the port specified.

        The vision sensor has a resolution of 316x212 pixels.

        Parameters
        - index: The port index for this vision. The index is zero based.
        - brightness: The vision sensor brightness seting. Values are 0 to 255.
        - signatures: List of signature objects
                      used to setup the detection signatures for this sensor.
    """)
    def __init__(self, index: Ports,
                 brightness: Optional[int] = None,
                 signatures: Optional[list] = None, /):
        """Initialize Vision Sensor."""
        self.port: Ports = index
        self.brightness: Optional[int] = brightness
        self.signatures: Optional[list] = signatures

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, Vision) and
                (other.port == self.port) and
                (other.brightness == self.brightness) and
                (other.signatures == self.signatures))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.port, self.brightness, self.signatures))

    @robotmesh_doc("""
        Take a data sample from the vision sensor.

        Parameters
        - id: The signature id or color code of the object to look for.
        - count: the amount of objects to look for.
                 The largest of the object will be returned. Optional.

        Returns:
        The number of objects found from the ID passed in the parameter.
    """)
    @vexcode_doc("""
        Snapshot

        Takes a snapshot from a VEX Vision Sensor.

        The snapshot command will capture the current image from Vision Sensor
        to be processed and analyzed for color signatures and codes.

        Typically, a snapshot is required first before using any other
        Vision Sensor commands.
    """)
    @sense
    def take_snapshot(self, signature_id: int,
                      count: Optional[int] = None, /) -> int:
        """Take snapshot of current scene."""

    @robotmesh_doc("""
        Number of objects found in the data sample.
    """)
    @property
    def object_count(self) -> int:
        """Return number of objects detected."""

    @robotmesh_doc("""
        List of the largest objects found in the data sample.
    """)
    @property
    def objects(self) -> list[VisionObject]:
        """Return detected objects."""

    @robotmesh_doc("""
        Largest object found in the data sample.
    """)
    @vexcode_doc("""
        Largest Object

        Reports information about the largest detected object
        from a VEX Vision Sensor.

        Configure the Vision Sensor by adding signatures / codes.

        A call to the Vision Sensor's Take Snapshot command is then required to
        capture an image in the Vision Sensor prior to
        using the Largest Object command.

        The following is a list of properties that can be accessed on
        the object returned by the Largest Object command:
        - id: A unique ID assigned to each object by the Vision Sensor
        - originX: The top left X position of the object
        - originY: The top left Y position of the object
        - centerX: The center X position of the object
        - centerY: The center Y position of the object
        - width: The width of the object
        - height: The height of the object
        - angle: The angle of the object
        - exists: If the Vision Sensor detects the object or not
    """)
    @property
    def largest_object(self) -> VisionObject:
        """Return largest detected object."""
