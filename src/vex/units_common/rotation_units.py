"""Rotation Units."""


from collections.abc import Sequence
from enum import IntEnum

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('RotationUnits',)


@robotmesh_doc("""
    The measurement units for rotation values.
""")
class RotationUnits(IntEnum):
    """Rotation Units."""

    DEG: int = 0   # A rotation unit that is measured in degrees.
    REV: int = 1   # A rotation unit that is measured in revolutions.
    RAW: int = 99   # A rotation unit that is measured in raw data form.
