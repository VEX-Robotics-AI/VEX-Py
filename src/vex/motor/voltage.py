"""Voltage units."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = ('VoltageUnits',)


@robotmesh_doc("""
    Measurement units for voltage values

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_voltage_units.html
""")
class VoltageUnits(IntEnum):
    """Voltage units."""

    VOLT: int = 0
    MV: int = 1
