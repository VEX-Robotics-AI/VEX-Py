"""Measurement with Unit abstract base class."""


from collections.abc import Sequence
from dataclasses import dataclass
from enum import IntEnum
from typing import Literal, LiteralString

from .._common_enums.percent import PercentUnits, PERCENT
from .type import Num


__all__: Sequence[LiteralString] = ('_MeasurementWithUnitABC',)


@dataclass
class _MeasurementWithUnitABC:
    measurement: Num
    unit: IntEnum | PercentUnits | Literal[PERCENT]
