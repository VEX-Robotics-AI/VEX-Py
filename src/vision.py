"""VEX Vision Sensor.

Robot Mesh Python B:
robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevision.html
"""


from __future__ import annotations

from collections.abc import Sequence
from typing import Optional
from typing_extensions import Self

from abm.decor import sense

from vex._abstract_device import Device
from vex import Ports

# pylint: disable=unused-import
from vex.util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = 'Vision', 'VisionObject'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvision_1_1_vision.html
""")
class Vision(Device):
    """VEX Vision Sensor."""

    @robotmesh_doc("""
        Create a new vision object on the port specified.

        The vision sensor has a resolution of 316x212 pixels.

        Parameters:
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
        """Check Equality."""
        return (isinstance(other, Vision) and
                (other.port == self.port) and
                (other.brightness == self.brightness) and
                (other.signatures == self.signatures))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.port, self.brightness, self.signatures))

    @robotmesh_doc("""
        Take a data sample from the vision sensor.

        Parameters:
        - id: The signature id or color code of the object to look for.
        - count: the amount of objects to look for.
                 The largest of the object will be returned. Optional.

        Returns:
        The number of objects found from the ID passed in the parameter.
    """)
    @sense
    def take_snapshot(self, id: int,   # pylint: disable=redefined-builtin
                      count: Optional[int] = None, /) -> int:
        """Take Snapshot of current scene."""

    @robotmesh_doc("""
        Return number of objects found in the data sample.
    """)
    @property
    def object_count(self) -> int:
        """Return Number of Objects Detected."""

    @robotmesh_doc("""
        Return list of the largest objects found in the data sample.
    """)
    @property
    def objects(self) -> list[VisionObject]:
        """Return Detected Objects."""

    @robotmesh_doc("""
        Return the largest object found in the data sample.
    """)
    @property
    def largest_object(self) -> VisionObject:
        """Return Largest Deteced Object."""


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvision_1_1_vision_object.html
""")
class VisionObject:
    """Vision Object."""

    @robotmesh_doc("""
        Return the unique ID of the object.
    """)
    @property
    def id(self) -> int:
        """Return Object ID."""

    @robotmesh_doc("""
        Return the top left x position of the object.
    """)
    @property
    def originX(self) -> int:
        """Return Object's Top-Left X Co-ordinate."""

    @robotmesh_doc("""
        Return the top left y position of the object.
    """)
    @property
    def originY(self) -> int:
        """Return Object's Top-Left Y Co-ordinate."""

    @robotmesh_doc("""
        Return the center x position of the object.
    """)
    @property
    def centerX(self) -> int:
        """Return Object's Center X Co-ordinate."""

    @robotmesh_doc("""
        Return the center y position of the object.
    """)
    @property
    def centerY(self) -> int:
        """Return Object's Center Y Co-ordinate."""

    @robotmesh_doc("""
        Return the width of the object.
    """)
    @property
    def width(self) -> int:
        """Return Object's Width."""

    @robotmesh_doc("""
        Return the height of the object.
    """)
    @property
    def height(self) -> int:
        """Return Object's Height."""

    @robotmesh_doc("""
        Return the angle of the object.
    """)
    @property
    def angle(self) -> int:
        """Return Object's Angle."""

    @robotmesh_doc("""
        Return True if vision sensor detects the object, False if not.
    """)
    @property
    def exists(self) -> bool:
        """Check if Object is detected."""
