"""Controller types."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = 'ControllerType', 'PRIMARY', 'PARTNER'


@robotmesh_doc("""
    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_controller_type.html
""")
class ControllerType(IntEnum):
    """Controller types."""

    PRIMARY: int = 0
    PARTNER: int = 1


# aliases
PRIMARY: ControllerType = ControllerType.PRIMARY
PARTNER: ControllerType = ControllerType.PARTNER
