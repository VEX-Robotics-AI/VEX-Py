"""Numeric Units."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('NumericUnits',)


class NumericUnits(IntEnum):
    """Numeric Units."""

    PERCENT: int = auto()


# aliases
PERCENT = NumericUnits.PERCENT
