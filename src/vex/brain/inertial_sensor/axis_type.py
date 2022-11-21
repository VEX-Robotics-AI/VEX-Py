"""Axis Types."""


from collections.abc import Sequence
from enum import IntEnum, auto

from ..._util.doc import vexcode_doc


__all__: Sequence[str] = 'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS'


@vexcode_doc("""
    VEX IQ (2nd generation) Axis Types.
""")
class AxisType(IntEnum):
    """VEX IQ (2nd generation) Axis Types."""

    # reports acceleration of forward-to-backward movements
    XAXIS: int = auto()

    # reports acceleration of side-to-side movements
    YAXIS: int = auto()

    # reports acceleration of up-to-down movements
    ZAXIS: int = auto()


# aliases
XAXIS: AxisType = AxisType.XAXIS
YAXIS: AxisType = AxisType.YAXIS
ZAXIS: AxisType = AxisType.ZAXIS
