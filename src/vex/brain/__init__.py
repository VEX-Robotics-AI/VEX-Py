"""VEX Brain."""


from __future__ import annotations

from collections.abc import Sequence

from .._abstract_device import SingletonDevice
from .button import BrainButton
from .screen import BrainLcd
from .sound import BrainSound, NoteType, SoundType
from ..time import TimeUnits
from .timer import BrainTimer

from ..util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = (
    "Brain",
    "BrainButton",
    "BrainLcd",
    "BrainSound",
    "NoteType",
    "SoundType",
)


@robotmesh_doc(
    """
    Use the Brain class to see battery information, or write to the screen.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain.html
"""
)
class Brain(SingletonDevice):
    """VEX Brain."""

    def __init__(self):
        """Initialize Brain."""
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id="CHECK")
        self._buttonUp: BrainButton = BrainButton(id="UP")
        self._buttonDown: BrainButton = BrainButton(id="DOWN")
        self._sound: BrainSound = BrainSound()
        self._timer: BrainTimer = BrainTimer()

    @property
    def screen(self) -> BrainLcd:
        """Brain LCD."""
        return self._screen

    @property
    def buttonCheck(self) -> BrainButton:
        """Brain Button CHECK."""
        return self._buttonCheck

    @property
    def buttonUp(self) -> BrainButton:
        """Brain Button UP."""
        return self._buttonUp

    @property
    def buttonDown(self) -> BrainButton:
        """Brain Button DOWN."""
        return self._buttonDown

    @property
    def sound(self) -> BrainSound:
        """Brain Sound."""
        return self._sound

    @property
    def timer(self) -> BrainTimer:
        """Brain Timer."""
        return self._timer

    @vexcode_doc(
        """
        Play a musical note on the speaker.

        Parameters:
        - note: musical note to play: NoteType enum value
        """
    )
    def play_sound(self, note: NoteType):
        """Play a musical note on the speaker."""
        return self.sound.play(note)

    @vexcode_doc(
        """
        Play a musical note on the speaker.

        Parameters:
        - note: musical note to play: NoteType enum value
        - octave: octave of the note [1-7], optional.
        - duration: time. 0 to start playing without blocking. Default 0.5 ms.
        """
    )
    def play_note(self, note: NoteType, octave: int = 3, duration: float = 0.5):
        """Play a musical note on the speaker."""
        return self.sound.play(note, octave, duration, TimeUnits.MSEC)
