"""Measurement with Unit abstract base class."""


from collections.abc import Sequence
from dataclasses import dataclass
from enum import IntEnum
from typing import LiteralString

from .._util.type import Num


__all__: Sequence[LiteralString] = ('_MeasurementWithUnitABC',)


@dataclass
class _MeasurementWithUnitABC:
    measurement: Num
    unit: IntEnum
