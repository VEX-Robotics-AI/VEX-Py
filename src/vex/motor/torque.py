"""Torque units."""


from collections.abc import Sequence
from enum import IntEnum, auto
from typing import LiteralString

from .._common_enums.percent import PERCENT

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('TorqueUnits',)


@robotmesh_doc("""
    The measurement units for torque values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_torque_units.html
""")
class TorqueUnits(IntEnum):
    """Torque units."""

    PCT: int = PERCENT
    NM: int = auto()  # torque unit measured in Newton Meters
    IN_LB: int = auto()  # torque unit measured in Inch Pounds
