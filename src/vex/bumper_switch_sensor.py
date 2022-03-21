"""VEX Bumper Switch Sensor."""


from collections.abc import Sequence

from __vex_decor import sense

from .abstract import Device
from .port import Ports


__all__: Sequence[str] = ('Bumper',)


class Bumper(Device):
    """Bumper Switch Sensor."""

    def __init__(self, index: Ports):
        """
        Create a new bumper object on the port specified in the parameter.

        param:
        index: The port index for this bumper. The index is zero-based.
        """
        self.port: Ports = index

    @sense
    def pressing(self) -> bool:
        """
        Get the pressed status of the bumper device.

        Returns
        True if pressed, False otherwise.
        """
