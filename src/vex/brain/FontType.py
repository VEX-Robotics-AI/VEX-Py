"""Touch LED Color."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import vexcode_doc


__all__: Sequence[str] = ('FontType',)


@vexcode_doc("""
    
Defined font types.

""")
class FontType(IntEnum):
    """Font Type"""

    MONO12: int = 0
    MONO15: int = 1
    MONO20: int = 2
    MONO30: int = 3
    MONO40: int = 4
    MONO60: int = 5
    PROP20: int = 6
    PROP30: int = 7
    PROP40: int = 8
    PROP60: int = 9
    