"""Current Units."""

from collections.abc import Sequence
from enum import IntEnum, auto

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = 'CurrentUnits', 'AMP'


@robotmesh_doc("""
    VEXcode API CurrentUnits.
""")
class CurrentUnits(IntEnum):
    """Current Units."""

    AMP: int = auto()   # A current unit that is measured in amps.


# aliases
AMP: CurrentUnits = CurrentUnits.AMP
