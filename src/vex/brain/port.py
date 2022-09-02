"""Ports."""


from collections.abc import Sequence
from enum import IntEnum

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('Ports',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_ports.html
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
