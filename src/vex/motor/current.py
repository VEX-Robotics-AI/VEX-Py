"""Current Units."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString


__all__: Sequence[LiteralString] = ('CurrentUnits',)


class CurrentUnits(IntEnum):
    """Current Units."""

    AMP: int = auto()
