"""Current Units."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = ('CurrentUnits',)


class CurrentUnits(IntEnum):
    """Current Units."""

    AMP: int = auto()
