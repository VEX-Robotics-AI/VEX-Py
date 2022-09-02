"""Movement Direction Types."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = ('DirectionType',)


@robotmesh_doc("""
    The defined units for direction values.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_direction_type.html
""")
class DirectionType(IntEnum):
    """Movement Direction Types."""

    FWD: int = 0   # A direction unit that is defined as forward.
    REV: int = 1   # A direction unit that is defined as backward.
