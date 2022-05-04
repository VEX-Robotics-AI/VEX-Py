"""VEX Abstract Base Classes."""


from __future__ import annotations

from collections.abc import Sequence

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

    def __eq__(self, other: Device) -> bool:
        """Check Equality."""
        return isinstance(other, type(self)) and (other.port == self.port)

    def __repr__(self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.port.name})'


class SingletonDevice:   # pylint: disable=too-few-public-methods
    """Singleton Device."""

    def __eq__(self, other: SingletonDevice) -> bool:
        """Check Equality."""
        return isinstance(other, type(self))

    def __repr__(self) -> str:
        """Return string representation."""
        return type(self).__name__
