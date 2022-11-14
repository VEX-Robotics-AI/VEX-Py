"""Rotation Units."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = 'RotationUnits', 'DEGREES', 'TURNS'


@robotmesh_doc("""
    The measurement units for rotation values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_rotation_units.html
""")
class RotationUnits(IntEnum):
    """Rotation Units."""

    DEG: int = 0   # A rotation unit that is measured in degrees
    REV: int = 1   # A rotation unit that is measured in revolutions
    RAW: int = 99   # A rotation unit that is measured in raw data form


# aliases
DEGREES: RotationUnits = RotationUnits.DEG
TURNS: RotationUnits = RotationUnits.REV
