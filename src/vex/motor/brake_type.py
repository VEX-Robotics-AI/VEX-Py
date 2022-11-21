"""Motor Brake Types."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'BrakeType', 'COAST', 'BRAKE', 'HOLD'


@robotmesh_doc("""
    The defined units for brake values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brake_type.html
""")
class BrakeType(IntEnum):
    """Motor Brake Types."""

    COAST: int = 0   # A brake unit that is defined as coast
    BRAKE: int = 1   # A brake unit that is defined as brake
    HOLD: int = 2   # A brake unit that is defined as hold


# aliases
COAST: BrakeType = BrakeType.COAST
BRAKE: BrakeType = BrakeType.BRAKE
HOLD: BrakeType = BrakeType.HOLD
