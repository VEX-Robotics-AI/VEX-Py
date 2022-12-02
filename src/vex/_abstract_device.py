"""Abstract Device Base Classes."""


from collections.abc import Sequence
from typing_extensions import Self

from .brain.port import Ports

from ._util.doc import robotmesh_doc


__all__: Sequence[str] = 'Device', 'SingletonDevice'


@robotmesh_doc("""
    Base class for all VEX devices.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_device.html
""")
class Device:
    """Base Device Class."""

    @property
    def port(self) -> Ports:
        """Port."""
        return self._port

    @port.setter
    def port(self, port: Ports):
        self._port: Ports = port

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, type(self)) and (other.port == self.port)

    def __hash__(self) -> int:
        """Return integer hash."""
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.port.name})'


class SingletonDevice:
    """Singleton Device."""

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, type(self))

    def __hash__(self) -> int:
        """Return integer hash."""
        return 0

    def __repr__(self) -> str:
        """Return string representation."""
        return type(self).__name__
