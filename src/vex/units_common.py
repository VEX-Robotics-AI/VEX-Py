"""Measurement Units."""


from collections.abc import Sequence
from enum import IntEnum


__all__: Sequence[str] = 'DistanceUnits', 'RotationUnits'


class DistanceUnits(IntEnum):
    """The measurement units for distance values."""

    MM: int = 0   # A distance unit that is measured in millimeters.
    IN: int = 1   # A distance unit that is measured in inches.
    CM: int = 2   # A distance unit that is measured in centimeters.


class RotationUnits(IntEnum):
    """The measurement units for rotation values."""

    DEG: int = 0   # A rotation unit that is measured in degrees.
    REV: int = 1   # A rotation unit that is measured in revolutions.
    RAW: int = 99   # A rotation unit that is measured in raw data form.
