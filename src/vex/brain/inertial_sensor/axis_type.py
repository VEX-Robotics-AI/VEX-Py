"""Axis Types."""


from collections.abc import Sequence
from enum import IntEnum, auto

from ...util.doc import vexcode_doc


__all__: Sequence[str] = ('AxisType',)


@vexcode_doc("""
    VEX IQ (2nd generation) Axis types.
""")
class AxisType(IntEnum):
    """VEX IQ (2nd generation) Axis types."""

    # reports acceleration of forward-to-backward movements
    XAXIS: int = auto()

    # reports acceleration of side-to-side movements
    YAXIS: int = auto()

    # reports acceleration of up-to-down movements
    ZAXIS: int = auto()
