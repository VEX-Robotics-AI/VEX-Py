from __future__ import annotations

from typing import Optional

from vex import Device, Ports


class Vision(Device):
    def __init__(
            self,
            index: Ports,
            brightness: Optional[int] = None,
            signatures: Optional[list] = None):
        """
        Creates a new vision object on the port specified.

        The vision sensor has a resolution of 316x212 pixels.

        Parameters:
        - index: The port index for this vision. The index is zero based.
        - brightness: The vision sensor brightness seting. Values are 0 to 255.
        - signatures: List of signature objects
                      used to setup the detection signatures for this sensor.
        """
        self.port = index
        self.brightness = brightness
        self.signatures = signatures

    def take_snapshot(self, id: int, count: Optional[int] = None) -> int:
        """
        Takes a data sample from the vision sensor.

        Parameters:
        - id: The signature id or color code of the object to look for.
        - count: the amount of objects to look for.
                 The largest of the object will be returned. Optional.

        Returns:
        The number of objects found from the ID passed in the parameter.
        """

    @property
    def object_count(self) -> int:
        """
        Number of objects found in the data sample.
        """

    @property
    def objects(self) -> list[VisionObject]:
        """
        List of the largest objects found in the data sample.
        """

    @property
    def largest_object(self) -> VisionObject:
        """
        The largest object found in the data sample.
        """


class VisionObject:
    @property
    def id(self) -> int:
        """
        The unique ID of the object.
        """

    @property
    def originX(self) -> int:
        """
        The top left x position of the object.
        """

    @property
    def originY(self) -> int:
        """
        The top left y position of the object.
        """

    @property
    def centerX(self) -> int:
        """
        The center x position of the object.
        """

    @property
    def centerY(self) -> int:
        """
        The center y position of the object.
        """

    @property
    def width(self) -> int:
        """
        The width of the object.
        """

    @property
    def height(self) -> int:
        """
        The height of the object.
        """

    @property
    def angle(self) -> int:
        """
        The angle of the object.
        """

    @property
    def exists(self) -> bool:
        """
        True if the vision sensor detects the object, False if not.
        """
