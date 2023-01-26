"""Font Types."""


from collections.abc import Sequence
from enum import IntEnum, auto

from ..._util.doc import robotmesh_doc


__all__: Sequence[str] = (
    'Font',
    'MONO_M', 'MONO_L', 'MONO_XL', 'MONO_XXL', 'MONO_S', 'MONO_XS',
    'PROP_M', 'PROP_L', 'PROP_XL', 'PROP_XXL',
    'FontType')


@robotmesh_doc("""
    Unit of font type

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_font.html
""")
class Font(IntEnum):
    """Fonts."""

    MONO_20: int = 0  # represents a type of font as mono20
    MONO_30: int = 1  # represents a type of font as mono30
    MONO_40: int = 2  # represents a type of font as mono40
    MONO_60: int = 3  # represents a type of font as mono60

    PROP_20: int = 4  # represents a type of font as prop20
    PROP_30: int = 5  # represents a type of font as prop30
    PROP_40: int = 6  # represents a type of font as prop40
    PROP_60: int = 7  # represents a type of font as prop60

    MONO_15: int = 8  # represents a type of font as mono15
    MONO_12: int = 9  # represents a type of font as mono12

    CHINESE_16: int = 0xf0  # font supporting Chinese characters


# aliases
MONO_M: Font = Font.MONO_20
MONO_L: Font = Font.MONO_30
MONO_XL: Font = Font.MONO_40
MONO_XXL: Font = Font.MONO_60
MONO_S: Font = Font.MONO_15
MONO_XS: Font = Font.MONO_12

PROP_M: Font = Font.PROP_20
PROP_L: Font = Font.PROP_30
PROP_XL: Font = Font.PROP_40
PROP_XXL: Font = Font.PROP_60


class FontType(IntEnum):
    """Font Types."""

    MONO12: int = auto()
    MONO15: int = auto()
    MONO20: int = auto()
    MONO30: int = auto()
    MONO40: int = auto()
    MONO60: int = auto()
    PROP20: int = auto()
    PROP30: int = auto()
    PROP40: int = auto()
    PROP60: int = auto()
