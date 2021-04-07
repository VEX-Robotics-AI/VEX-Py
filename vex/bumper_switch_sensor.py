from __decor import return_qualname_and_args

from .abstract import Device
from .port import Ports


@return_qualname_and_args
class Bumper(Device):
    def __init__(self, index: Ports):
        """
        Creates a new bumper object on the port specified in the parameter.

        param:
        index: The port index for this bumper. The index is zero-based.
        """
        self.port = index
        self._pressing = False

    def pressing(self) -> bool:
        """
        Get the pressed status of the bumper device.

        Returns
        True if pressed, False otherwise.
        """
        return self._pressing
