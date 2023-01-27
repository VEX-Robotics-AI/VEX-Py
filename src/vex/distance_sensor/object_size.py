"""Object size types."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString


__all__: Sequence[LiteralString] = ('ObjectSizeType',)


class ObjectSizeType(IntEnum):
    """Object size types."""

    SMALL: int = auto()
    MEDIUM: int = auto()
    LARGE: int = auto()
