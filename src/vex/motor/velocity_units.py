"""Velocity Units."""


from __future__ import annotations

from collections.abc import Sequence
from enum import IntEnum

from ..units_common.numeric import PERCENT
from ..util.doc import robotmesh_doc


__all__: Sequence[str] = 'VelocityUnits', 'RPM', 'DPS'


@robotmesh_doc("""
    The measurement units for velocity values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_velocity_units.html
""")
class VelocityUnits(IntEnum):
    """Velocity Units."""

    PCT: int = PERCENT   # A velocity unit that is measured in percentage.
    RPM: int = 1   # A velocity unit that is measured in rotations per minute.
    DPS: int = 2   # A velocity unit that is measured in degrees per second.
    RAW: int = 99   # A velocity unit that is measured in raw data form.


# aliases
RPM: VelocityUnits = VelocityUnits.RPM
DPS: VelocityUnits = VelocityUnits.DPS
