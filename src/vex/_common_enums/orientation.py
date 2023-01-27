"""Inertial Orientation Types."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = 'OrientationType', 'ROLL', 'PITCH', 'YAW'


@robotmesh_doc("""
    Unit for inertial sensor orientation

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_orientation_type.html
""")
class OrientationType(IntEnum):
    """Inertial Orientation Types."""

    ROLL: int = 0  # rotation around front-to-back axis
    PITCH: int = 1  # rotation around side-to-side axis
    YAW: int = 2  # rotation around the vertical axis


# aliases
ROLL: OrientationType = OrientationType.ROLL
PITCH: OrientationType = OrientationType.PITCH
YAW: OrientationType = OrientationType.YAW
