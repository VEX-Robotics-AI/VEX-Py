"""Efficiency."""


from collections.abc import Sequence
from typing import Literal, LiteralString

from .._common_enums.percent import PERCENT
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = ('_Efficiency',)


class _Efficiency(_MeasurementWithUnitABC):
    measurement: float
    unit: Literal[PERCENT] = PERCENT
