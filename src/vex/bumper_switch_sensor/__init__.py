"""VEX Bumper Switch Sensor."""


from collections.abc import Sequence

from abm.decor import sense

from .._abstract_device import Device
from ..brain.port import Ports

# pylint: disable=unused-import
from ..util.doc import vexcode_doc   # noqa: F401
 

__all__: Sequence[str] = ('Bumper')


class Bumper(Device):
    """Bumper Switch Sensor."""

    @vexcode_doc("""
        Create a new bumper object on the port specified in the parameter.

        param: 
        index: The port index for this bumper. The index is zero-based.
    """
    )
    def __init__(self, index: Ports, /):
        """Initialize Bumper Switch Sensor."""
        self.port: Ports = index

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash(self.port)

    @vexcode_doc("""
        Get the pressed status of the bumper device.

        Returns
        True if pressed, False otherwise.
    """ 
    )

    @sense
    def pressing(self) -> bool:
        """Return Bumper's pressed status."""

   


