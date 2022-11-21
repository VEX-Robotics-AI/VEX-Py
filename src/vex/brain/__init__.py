"""Brain."""


from __future__ import annotations

from collections.abc import Sequence

from .._abstract_device import SingletonDevice

from .._util.doc import robotmesh_doc

from .battery import BrainBattery
from .button import BrainButton
from .screen import BrainLcd, FontType
from .speaker import BrainSound, NoteType, SoundType
from .timer import BrainTimer


__all__: Sequence[str] = ('Brain',
                          'BrainBattery',
                          'BrainButton',
                          'BrainLcd', 'FontType',
                          'BrainSound', 'NoteType', 'SoundType')


@robotmesh_doc("""
    Use the Brain class to see battery information, or write to the screen.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain.html
""")
class Brain(SingletonDevice):
    """Brain."""

    def __init__(self):
        """Initialize Brain."""
        self._battery: BrainBattery = BrainBattery()
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id="CHECK")
        self._buttonUp: BrainButton = BrainButton(id="UP")
        self._buttonDown: BrainButton = BrainButton(id="DOWN")
        self._sound: BrainSound = BrainSound()
        self._timer: BrainTimer = BrainTimer()

    @property
    def battery(self) -> BrainBattery:
        """Brain Battery."""
        return self._battery

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

    def play_sound(self, sound: SoundType = SoundType.SIREN, /):
        """Play a sound effect."""
        self.sound.play_sound(sound)

    def play_note(self, octave: int = 3, note: int = 0, duration: int = 1000):
        """Play a musical note."""
        self.sound.play_note(octave, note, duration)

    @property
    def timer(self) -> BrainTimer:
        """Brain Timer."""
        return self._timer
