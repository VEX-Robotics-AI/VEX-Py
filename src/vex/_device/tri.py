"""3-Wire Device abstract base class."""


from collections.abc import Sequence
from typing import LiteralString

from .._util.doc import robotmesh_doc
from ._abc import Device


__all__: Sequence[LiteralString] = ('TriDevice',)


@robotmesh_doc("""
    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_tri_device.html
""")
class TriDevice(Device):
    # pylint: disable=abstract-method,too-few-public-methods
    """3-Wire Device."""
