"""Device abstract base class."""


from __future__ import annotations

from collections.abc import Sequence
from typing import LiteralString, Self, TYPE_CHECKING

from ..brain.port import Ports

from .._util.doc import robotmesh_doc

if TYPE_CHECKING:
    from .v5 import V5DeviceType


__all__: Sequence[LiteralString] = ('Device',)


@robotmesh_doc("""
    Base class for all VEX devices
    Use the device class to get information about a vex device plugged into VEX

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_device.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_device.html
""")
class Device:
    """Base Device class."""

    @property
    def port(self: Self, /) -> Ports:
        """Port."""
        return self._port

    @port.setter
    def port(self: Self, port: Ports, /):
        self._port: Ports = port

    def __eq__(self: Self, other: Self, /) -> bool:
        """Check equality."""
        return isinstance(other, type(self)) and (other.port == self.port)

    def __hash__(self: Self, /) -> int:
        """Return integer hash."""
        raise NotImplementedError

    def __repr__(self: Self, /) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.port.name})'

    def type(self, /) -> V5DeviceType:
        """Return type of device, for V5 case only."""
