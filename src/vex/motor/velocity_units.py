"""Velocity Units."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = ('VelocityUnits',)


@robotmesh_doc("""
    The measurement units for velocity values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_velocity_units.html
""")
class VelocityUnits(IntEnum):
    """Velocity Units."""

    PCT: int = 0   # A velocity unit that is measured in percentage.
    RPM: int = 1   # A velocity unit that is measured in rotations per minute.
    DPS: int = 2   # A velocity unit that is measured in degrees per second.
    RAW: int = 99   # A velocity unit that is measured in raw data form.