"""Power units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'PowerUnits', '_Power'


@robotmesh_doc("""
    Power units

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_power_units.html
""")
class PowerUnits(IntEnum):
    """Power units."""

    WATT: int = 0  # unit representing values of power in watts


class _Power(_MeasurementWithUnitABC):  # pylint: disable=too-few-public-methods
    unit: PowerUnits = PowerUnits.WATT
