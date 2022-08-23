"""VEX Vision Sensor."""


from __future__ import annotations

from collections.abc import Sequence
from typing import Optional

from __vex.decor import sense

from vex import Device, Ports


__all__: Sequence[str] = 'Vision', 'VisionObject'


class Vision(Device):
    """VEX Vision Sensor."""

    def __init__(
            self, index: Ports,
            brightness: Optional[int] = None,
            signatures: Optional[list] = None):
        """
        Create a new vision object on the port specified.

        The vision sensor has a resolution of 316x212 pixels.

        Parameters:
        - index: The port index for this vision. The index is zero based.
        - brightness: The vision sensor brightness seting. Values are 0 to 255.
        - signatures: List of signature objects
                      used to setup the detection signatures for this sensor.
        """
        self.port: Ports = index
        self.brightness: Optional[int] = brightness
        self.signatures: Optional[list] = signatures

    @sense
    def take_snapshot(self,
                      id: int,   # pylint: disable=redefined-builtin
                      count: Optional[int] = None) -> int:
        """
        Take a data sample from the vision sensor.

        Parameters:
        - id: The signature id or color code of the object to look for.
        - count: the amount of objects to look for.
                 The largest of the object will be returned. Optional.

        Returns:
        The number of objects found from the ID passed in the parameter.
        """

    @property
    def object_count(self) -> int:
        """Return number of objects found in the data sample."""

    @property
    def objects(self) -> list[VisionObject]:
        """Return list of the largest objects found in the data sample."""

    @property
    def largest_object(self) -> VisionObject:
        """Return the largest object found in the data sample."""


class VisionObject:
    """Vision Object."""

    @property
    def id(self) -> int:
        """Return the unique ID of the object."""

    @property
    def originX(self) -> int:
        """Return the top left x position of the object."""

    @property
    def originY(self) -> int:
        """Return the top left y position of the object."""

    @property
    def centerX(self) -> int:
        """Return the center x position of the object."""

    @property
    def centerY(self) -> int:
        """Return the center y position of the object."""

    @property
    def width(self) -> int:
        """Return the width of the object."""

    @property
    def height(self) -> int:
        """Return the height of the object."""

    @property
    def angle(self) -> int:
        """Return the angle of the object."""

    @property
    def exists(self) -> bool:
        """Return True if vision sensor detects the object, False if not."""
