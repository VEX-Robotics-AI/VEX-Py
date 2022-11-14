"""Object Size Types."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('ObjectSizeType',)


class ObjectSizeType(IntEnum):
    """Object Size Types."""

    SMALL: int = auto()
    MEDIUM: int = auto()
    LARGE: int = auto()
