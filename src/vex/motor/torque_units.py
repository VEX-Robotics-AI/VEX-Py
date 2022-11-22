"""Torque Units."""


from collections.abc import Sequence
from enum import IntEnum, auto

from .._common_enums.numeric import PERCENT

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = ('TorqueUnits',)


@robotmesh_doc("""
    The measurement units for torque values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_torque_units.html
""")
class TorqueUnits(IntEnum):
    """Torque Units."""

    PCT: int = PERCENT
    NM: int = auto()   # A torque unit that is measured in Newton Meters
    IN_LB: int = auto()   # A torque unit that is measured in Inch Pounds
