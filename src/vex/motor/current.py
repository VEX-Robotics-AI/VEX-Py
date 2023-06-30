"""Current units."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString

from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'CurrentUnits', '_Current'


class CurrentUnits(IntEnum):
    """Current units."""

    AMP: int = auto()


class _Current(_MeasurementWithUnitABC):
    unit: CurrentUnits = CurrentUnits.AMP
