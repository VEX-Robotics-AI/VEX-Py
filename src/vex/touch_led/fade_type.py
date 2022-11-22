"""Touch LED Fade Types."""


from collections.abc import Sequence
from enum import IntEnum

from .._util.doc import robotmesh_doc


__all__: Sequence[str] = ('FadeType',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_fade_type.html
""")
class FadeType(IntEnum):
    """Touch LED Fade Types."""

    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2
