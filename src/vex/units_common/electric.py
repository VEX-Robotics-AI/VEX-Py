"""Electric Current Units."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = 'CurrentUnits', 'AMP'


class CurrentUnits(IntEnum):
    """Current Units."""

    AMP: int = auto()


# aliases
AMP: CurrentUnits = CurrentUnits.AMP
