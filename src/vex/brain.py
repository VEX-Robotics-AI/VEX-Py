from __future__ import annotations

from enum import IntEnum

from __vex_decor import act, sense

from .abstract import SingletonDevice
from .time import TimeUnits


class Brain(SingletonDevice):
    """
    Use the Brain class to see battery information, or write to the screen.
    """

    def __init__(self):
        self._screen: BrainLcd = BrainLcd()
        self._buttonCheck: BrainButton = BrainButton(id='CHECK')
        self._buttonUp: BrainButton = BrainButton(id='UP')
        self._buttonDown: BrainButton = BrainButton(id='DOWN')
        self._sound: BrainSound = BrainSound()

    @property
    def screen(self) -> BrainLcd:
        return self._screen

    @property
    def buttonCheck(self) -> BrainButton:
        return self._buttonCheck

    @property
    def buttonUp(self) -> BrainButton:
        return self._buttonUp

    @property
    def buttonDown(self) -> BrainButton:
        return self._buttonDown

    @property
    def sound(self) -> BrainSound:
        return self._sound


class BrainButton:
    """
    Use the button class to get values from the brain's buttons.
    """

    def __init__(self, id: str):
        self.id: str = id

    def __str__(self) -> str:
        return f'{type(self).__name__}({self.id})'

    @sense
    def pressing(self) -> bool:
        """
        Gets the pressed status of a button.

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
        Prints a number, string, or boolean at a particular line,
        clearing the rest of the line.

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
        """
        Clears the whole screen.
        """


class BrainSound(SingletonDevice):
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
        play the wave sample

        Parameters:
        - waveType: type of the wave sample sound to play [0..15]
        - waitForCompletion: wait for the sample to finish playing
        """

    @act
    def play_melody(self, melody: str):
        """
        Play a melody form a string in a quasi musical alphabet notation
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
        set the sound effect type for subsequent notes played

        Parameters
        - effect: effect type [0..15]
        """
        self.sound_effect: int = effect

    @act
    def set_volume(self, volume: int):
        """
        set the sound volume [1-4]

        Parameters
        - volume: value [1=low...4=high]
        """
        self.volume: int = volume

    @act
    def stop(self):
        """
        Stop playing music.
        """


class NoteType(IntEnum):
    """
    Musical note to play.
    """
    silence: int = 0   # Stop playing/play a silence.
    C: int = 1
    D: int = 2
    E: int = 3
    F: int = 4
    G: int = 5
    A: int = 6
    B: int = 7
