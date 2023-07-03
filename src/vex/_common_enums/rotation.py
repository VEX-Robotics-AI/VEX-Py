"""Rotation units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'RotationUnits', 'DEGREES', 'TURNS', '_Rotation'  # noqa: E501


@robotmesh_doc("""
    Measurement units for rotation values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_rotation_units.html
""")
class RotationUnits(IntEnum):
    """Rotation units."""

    DEG: int = 0  # rotation unit measured in Degrees
    REV: int = 1  # rotation unit measured in Revolutions
    RAW: int = 99  # rotation unit measured in Raw Data Form


# aliases
DEGREES: RotationUnits = RotationUnits.DEG
TURNS: RotationUnits = RotationUnits.REV


class _Rotation(_MeasurementWithUnitABC):
    unit: RotationUnits = DEGREES
