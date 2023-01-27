"""Motor braking modes."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'BrakeType', 'COAST', 'BRAKE', 'HOLD'


@robotmesh_doc("""
    The defined units for brake values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brake_type.html
""")
class BrakeType(IntEnum):
    """Motor braking modes."""

    COAST: int = 0  # brake unit defined as Coast
    BRAKE: int = 1  # brake unit defined as Brake
    HOLD: int = 2  # brake unit defined as Hold


# aliases
COAST: BrakeType = BrakeType.COAST
BRAKE: BrakeType = BrakeType.BRAKE
HOLD: BrakeType = BrakeType.HOLD
