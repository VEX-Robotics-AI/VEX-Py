"""Ports."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('Ports',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_ports.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_ports.html
""")
class Ports(IntEnum):
    """Ports."""

    PORT1: int = 0
    PORT2: int = 1
    PORT3: int = 2
    PORT4: int = 3
    PORT5: int = 4
    PORT6: int = 5
    PORT7: int = 6
    PORT8: int = 7
    PORT9: int = 8
    PORT10: int = 9
    PORT11: int = 10
    PORT12: int = 11
    PORT13: int = 12
    PORT14: int = 13
    PORT15: int = 14
    PORT16: int = 15
    PORT17: int = 16
    PORT18: int = 17
    PORT19: int = 18
    PORT20: int = 19
    PORT21: int = 20
    PORT22: int = 21
