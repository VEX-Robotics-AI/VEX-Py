"""VEX Brain."""


from __future__ import annotations

from collections.abc import Sequence

from .._abstract_device import SingletonDevice
from .button import BrainButton
from .screen import BrainLcd
from .sound import BrainSound, NoteType, SoundType

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = (
    'Brain',
    'BrainButton',
    'BrainLcd',
    'BrainSound', 'NoteType', 'SoundType',
)


@robotmesh_doc("""
    Use the Brain class to see battery information, or write to the screen.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain.html
""")
class Brain(SingletonDevice):
    """VEX Brain."""

    def __init__(self):
        """Initialize Brain."""
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id='CHECK')
        self._buttonUp: BrainButton = BrainButton(id='UP')
        self._buttonDown: BrainButton = BrainButton(id='DOWN')
        self._sound: BrainSound = BrainSound()

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
