"""Torque units."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString

from .._common_enums.percent import PercentUnits, PERCENT

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'TorqueUnits', '_Torque'


@robotmesh_doc("""
    Measurement units for torque values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_torque_units.html
""")
class TorqueUnits(IntEnum):
    """Torque units."""

    PCT: int = PERCENT
    NM: int = auto()  # torque unit measured in Newton Meters
    IN_LB: int = auto()  # torque unit measured in Inch Pounds


class _Torque(_MeasurementWithUnitABC):
    unit: PercentUnits | TorqueUnits = PERCENT
