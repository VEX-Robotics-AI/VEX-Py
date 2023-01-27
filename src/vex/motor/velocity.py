"""Velocity units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._common_enums.percent import PERCENT

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'VelocityUnits', 'RPM', 'DPS'


@robotmesh_doc("""
    The measurement units for velocity values

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_velocity_units.html
""")
class VelocityUnits(IntEnum):
    """Velocity units."""

    PCT: int = PERCENT  # velocity unit measured in Percentage
    RPM: int = 1  # velocity unit measured in Rotations per Minute
    DPS: int = 2  # velocity unit measured in Degrees per Second
    RAW: int = 99  # velocity unit measured in Raw Data Form


# aliases
RPM: VelocityUnits = VelocityUnits.RPM
DPS: VelocityUnits = VelocityUnits.DPS
