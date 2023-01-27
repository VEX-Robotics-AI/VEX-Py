"""Sound effects."""


from collections.abc import Sequence
from enum import Enum, auto
from typing import LiteralString

from ..._util.doc import vexcode_doc


__all__: Sequence[LiteralString] = ('SoundType',)


@vexcode_doc("""
    Sound effects
""")
class SoundType(Enum):
    """Sound effects."""

    SIREN = auto()
    WRONG_WAY = auto()
    WRONG_WAY_SLOW = auto()
    FILLUP = auto()
    HEADLIGHTS_ON = auto()
    HEADLIGHTS_OFF = auto()
    TOLLBOOTH = auto()
    ALARM = auto()
    TADA = auto()
    DOOR_CLOSE = auto()
    RATCHET = auto()
    WRENCH = auto()
    SIREN2 = auto()
    RATCHET2 = auto()
    ALARM2 = auto()
    POWER_DOWN = auto()
