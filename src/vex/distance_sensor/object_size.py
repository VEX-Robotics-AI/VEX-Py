"""Object size types."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('ObjectSizeType',)


class ObjectSizeType(IntEnum):
    """Object size types."""

    SMALL: int = auto()
    MEDIUM: int = auto()
    LARGE: int = auto()
