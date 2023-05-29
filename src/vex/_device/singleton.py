"""Singleton Device abstract base class."""


from collections.abc import Sequence
from typing import LiteralString, Self


__all__: Sequence[LiteralString] = ('SingletonDevice',)


class SingletonDevice:
    """Singleton Device."""

    def __eq__(self: Self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, type(self))

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        return 0

    def __repr__(self: Self) -> LiteralString:
        """Return string representation."""
        return type(self).__name__
