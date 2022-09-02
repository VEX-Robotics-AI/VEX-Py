"""Brain Sound Speaker."""


from __future__ import annotations

from collections.abc import Sequence
from enum import Enum, IntEnum, auto

from abm.decor import act

from .._abstract import SingletonDevice
from ..time import TimeUnits

from ..util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = 'BrainSound', 'NoteType', 'SoundType'


class BrainSound(SingletonDevice):
    """Brain Sound."""

    @robotmesh_doc("""
        Play a musical note on the speaker.

        Parameters:
        - note: musical note to play: NoteType enum value
        - octave: octave of the note [1-7], optional
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
    """)
    @act
    def play(
            self, note: NoteType, octave: int = 3,
            duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC):
        """Play note/sound on Brain Sound Speaker."""

    @robotmesh_doc("""
        Play a musical note on the speaker.

        Parameters
        - note: musical note to play: 0=silence/stop, [1-56] numeric value
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
    """)
    @act
    def play_raw(
            self, note: NoteType,
            duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC):
        """Play note/sound on Brain Sound Speaker."""

    @robotmesh_doc("""
        Play the wave sample.

        Parameters:
        - waveType: type of the wave sample sound to play [0..15]
        - waitForCompletion: wait for the sample to finish playing
    """)
    @act
    def play_wave(self, waveType: int, waitForCompletion: bool = True):
        """Play WAV."""

    @robotmesh_doc("""
        Play a melody form a string in a quasi musical alphabet notation.

        (cdefgab)

        Parameters:
        - melody: string [cdefgab]: musical alphabet for notes,
                  space: pause,
                  +/-: increase/decrease octave of following notes
                  0-9: set duration of following notes
                       (in 1/8s: 1=eighth note...8 = full note)
    """)
    @act
    def play_melody(self, melody: str):
        """Play musical melody."""

    @robotmesh_doc("""
        Set the sound effect type for subsequent notes played.

        Parameters
        - effect: effect type [0..15]
    """)
    @act
    def set_sound_effect(self, effect: int):
        """Set Sound Effect."""
        # pylint: disable=attribute-defined-outside-init
        self.sound_effect: int = effect

    @robotmesh_doc("""
        Set the sound volume [1-4].

        Parameters
        - volume: value [1=low...4=high]
    """)
    @act
    def set_volume(self, volume: int):
        """Set Sound Volume."""
        # pylint: disable=attribute-defined-outside-init
        self.volume: int = volume

    @robotmesh_doc("""
        Stop playing music.
    """)
    @act
    def stop(self):
        """Stop Sound."""


@robotmesh_doc("""
    Musical note to play.
""")
class NoteType(IntEnum):
    """Musical Note."""

    silence: int = 0   # Stop playing/play a silence.
    C: int = 1
    D: int = 2
    E: int = 3
    F: int = 4
    G: int = 5
    A: int = 6
    B: int = 7


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
