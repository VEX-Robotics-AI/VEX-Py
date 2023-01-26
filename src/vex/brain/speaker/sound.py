"""Sound Effects."""


from collections.abc import Sequence
from enum import Enum, auto

from ..._util.doc import vexcode_doc


__all__: Sequence[str] = ('SoundType',)


@vexcode_doc("""
    Sound Effect
""")
class SoundType(Enum):
    """Sound Effect."""

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
