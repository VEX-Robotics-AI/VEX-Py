"""VEX Abstract Base Classes."""


from collections.abc import Sequence
from typing_extensions import Self   # pylint: disable=no-name-in-module

from .port import Ports


__all__: Sequence[str] = 'Device', 'SingletonDevice'


class Device:
    """Base class for all Vex IQ devices."""

    @property
    def port(self) -> Ports:
        """Port."""
        return self._port

    @port.setter
    def port(self, port: Ports):
        self._port = port

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, type(self)) and (other.port == self.port)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.port.name})'


class SingletonDevice:   # pylint: disable=too-few-public-methods
    """Singleton Device."""

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, type(self))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return 0

    def __repr__(self) -> str:
        """Return String Representation."""
        return type(self).__name__
