"""Torque units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import Literal, LiteralString

from .._common_enums.percent import PercentUnits, PERCENT

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'TorqueUnits', '_Torque'


@robotmesh_doc("""
    Measurement units for torque values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_torque_units.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_torque_units.html
""")
class TorqueUnits(IntEnum):
    """Torque units."""

    NM: int = 0  # torque unit measured in Newton Meters
    IN_LB: int = 1  # torque unit measured in Inch Pounds


class _Torque(_MeasurementWithUnitABC):  # pylint: disable=too-few-public-methods
    unit: TorqueUnits | PercentUnits | Literal[PERCENT] = PERCENT
