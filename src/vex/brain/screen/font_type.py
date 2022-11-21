"""Font Types."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('FontType',)


class FontType(IntEnum):
    """Font Types."""

    MONO12: int = auto()
    MONO15: int = auto()
    MONO20: int = auto()
    MONO30: int = auto()
    MONO40: int = auto()
    MONO60: int = auto()
    PROP20: int = auto()
    PROP30: int = auto()
    PROP40: int = auto()
    PROP60: int = auto()
