"""Turn directions."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'TurnType', 'LEFT', 'RIGHT'


@robotmesh_doc("""
    Left or right turn

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_turn_type.html
""")
class TurnType(IntEnum):
    """Turn directions."""

    LEFT: int = 0
    RIGHT: int = 1


# aliases
LEFT: TurnType = TurnType.LEFT
RIGHT: TurnType = TurnType.RIGHT
