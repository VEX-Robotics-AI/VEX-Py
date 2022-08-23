"""VEX Brain."""


from __future__ import annotations

from collections.abc import Sequence
from enum import IntEnum
from typing_extensions import Self   # pylint: disable=no-name-in-module

from __vex.decor import act, sense

from .abstract import SingletonDevice
from .time import TimeUnits


__all__: Sequence[str] = 'Brain', 'BrainButton', 'BrainLcd', 'BrainSound', 'NoteType'   # noqa: E501


class Brain(SingletonDevice):
    """Use the Brain class to see battery information, or write to the screen."""   # noqa: E501

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


class BrainButton:
    """Use the button class to get values from the brain's buttons."""

    def __init__(self, id: str):   # pylint: disable=redefined-builtin
        """Initialize BrainButton."""
        self.id: str = id

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, BrainButton) and (other.id == self.id)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash(self.id)

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.id})'

    @sense
    def pressing(self) -> bool:
        """
        Get the pressed status of a button.

        Returns
        True if pressed, False otherwise.
        """


class BrainLcd(SingletonDevice):
    """
    Use this class to write or draw to the brain's LCD screen.

    * 21 characters wide
    * 5 lines (1-5)
    """

    @act
    def print_line(self, number: int, text: str):
        """
        Print a number, string, or boolean at a particular line.

        (clearing the rest of the line)

        Parameters
        number: Line to print on, 1 is top line.
        text: object to print, usually a string.
              Use "" to clear the line.
              For multiple arguments, use format like
              "x: %g y: %g" % (x, y) -> "x: 123 y: 456"
              Supported format flags are g (all) x (hex) d (int) f (float)
        """

    @act
    def clear_screen(self):
        """Clear the whole screen."""


class BrainSound(SingletonDevice):
    """Brain Sound."""

    @act
    def play(
            self, note: NoteType, octave: int = 3,
            duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC):
        """
        Play a musical note on the speaker.

        Parameters:
        - note: musical note to play: NoteType enum value
        - octave: octave of the note [1-7], optional
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
        """

    @act
    def play_raw(
            self, note: NoteType,
            duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC):
        """
        Play a musical note on the speaker.

        Parameters
        - note: musical note to play: 0=silence/stop, [1-56] numeric value
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
        """

    @act
    def play_wave(self, waveType: int, waitForCompletion: bool = True):
        """
        Play the wave sample.

        Parameters:
        - waveType: type of the wave sample sound to play [0..15]
        - waitForCompletion: wait for the sample to finish playing
        """

    @act
    def play_melody(self, melody: str):
        """
        Play a melody form a string in a quasi musical alphabet notation.

        (cdefgab)

        Parameters:
        - melody: string [cdefgab]: musical alphabet for notes,
                  space: pause,
                  +/-: increase/decrease octave of following notes
                  0-9: set duration of following notes
                       (in 1/8s: 1=eighth note...8 = full note)
        """

    @act
    def set_sound_effect(self, effect: int):
        """
        Set the sound effect type for subsequent notes played.

        Parameters
        - effect: effect type [0..15]
        """
        # pylint: disable=attribute-defined-outside-init
        self.sound_effect: int = effect

    @act
    def set_volume(self, volume: int):
        """
        Set the sound volume [1-4].

        Parameters
        - volume: value [1=low...4=high]
        """
        # pylint: disable=attribute-defined-outside-init
        self.volume: int = volume

    @act
    def stop(self):
        """Stop playing music."""


class NoteType(IntEnum):
    """Musical note to play."""

    silence: int = 0   # Stop playing/play a silence.
    C: int = 1
    D: int = 2
    E: int = 3
    F: int = 4
    G: int = 5
    A: int = 6
    B: int = 7
