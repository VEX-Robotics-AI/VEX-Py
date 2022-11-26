"""Movement directions."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'DirectionType', 'FORWARD', 'REVERSE'


@robotmesh_doc("""
    The defined units for direction values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_direction_type.html
""")
class DirectionType(IntEnum):
    """Movement directions."""

    FWD: int = 0   # direction unit defined as Forward
    REV: int = 1   # direction unit defined as Backward


# aliases
FORWARD: DirectionType = DirectionType.FWD
REVERSE: DirectionType = DirectionType.REV
