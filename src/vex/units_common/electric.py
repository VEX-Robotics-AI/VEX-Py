"""Electric Current Units."""


from collections.abc import Sequence
from enum import IntEnum, auto


__all__: Sequence[str] = 'ElectricCurrentUnits', 'AMP'


class ElectricCurrentUnits(IntEnum):
    """Current Units."""

    AMP: int = auto()


# aliases
AMP: ElectricCurrentUnits = ElectricCurrentUnits.AMP
