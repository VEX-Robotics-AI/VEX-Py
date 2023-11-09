"""Efficiency."""


from collections.abc import Sequence
from typing import Literal, LiteralString

from .._common_enums.percent import PercentUnits, PERCENT
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = ('_Efficiency',)


class _Efficiency(_MeasurementWithUnitABC):  # pylint: disable=too-few-public-methods
    measurement: float
    unit: PercentUnits | Literal[PERCENT] = PERCENT
