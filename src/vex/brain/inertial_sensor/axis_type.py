"""Axis Types."""


from collections.abc import Sequence
from enum import IntEnum

from ...util.doc import vexcode_doc


__all__: Sequence[str] = ("AxisType",)


@vexcode_doc(
    """VEX IQ (2nd generation) Axis types.
    """
)
class AxisType(IntEnum):
    """VEX IQ (2nd generation) Axis types."""

    # reports acceleration of an Inertial Sensor's forward to backward movements.
    XAXIS: int = 0

    # reports acceleration of an Inertial Sensor's side to side movements
    YAXIS: int = 1

    # reports acceleration of an Inertial Sensor's up to down movements
    ZAXIS: int = 2
