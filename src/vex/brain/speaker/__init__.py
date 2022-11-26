"""Brain Sound Speaker."""


from __future__ import annotations

from collections.abc import Sequence

from abm.decor import act

from ..._abstract_device import SingletonDevice
from ...time import TimeUnits

from ..._util.doc import robotmesh_doc, vexcode_doc

from .note_type import NoteType
from .sound_type import SoundType


__all__: Sequence[str] = 'BrainSound', 'NoteType', 'SoundType'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain_sound.html
""")
class BrainSound(SingletonDevice):
    """Brain Sound Speaker."""

    @robotmesh_doc("""
        Set the sound effect type for subsequent notes played.

        Parameters
        - effect: effect type [0..15]
    """)
    def set_sound_effect(self, effect: int, /):
        """Set sound effect."""
        # pylint: disable=attribute-defined-outside-init
        self.sound_effect: int = effect

    @robotmesh_doc("""
        Set the sound volume [1-4].

        Parameters
        - volume: value [1=low...4=high]
    """)
    def set_volume(self, volume: int, /):
        """Set sound volume."""
        # pylint: disable=attribute-defined-outside-init
        self.volume: int = volume

    @vexcode_doc("""
        Play Sound

        Plays the specified sound effect.

        Replace the SOUND parameter with one of the following sounds to play:
        - SoundType.SIREN
        - SoundType.WRONG_WAY
        - SoundType.WRONG_WAY_SLOW
        - SoundType.FILLUP
        - SoundType.HEADLIGHTS_ON
        - SoundType.HEADLIGHTS_OFF
        - SoundType.TOLLBOOTH
        - SoundType.ALARM
        - SoundType.TADA
        - SoundType.DOOR_CLOSE
        - SoundType.RATCHET
        - SoundType.WRENCH
        - SoundType.SIREN2
        - SoundType.RATCHET2
        - SoundType.ALARM2
        - SoundType.POWER_DOWN

        Once a sound effect starts playing,
        the proceeding command will begin executing immediately.
    """)
    @act
    def play_sound(self, sound: SoundType, /):
        """Play sound effect."""

    @vexcode_doc("""
        Play Note

        Plays the selected musical note.

        Choose an octave to replace the OCTAVE parameter.
        The lowest is 1 and the highest is 7.

        Note: Octave is currently unsupported on IQ (2nd Generation) Brains

        Choose a note to replace the NOTE parameter:
        - 0 (C)
        - 1 (D)
        - 2 (E)
        - 3 (F)
        - 4 (G)
        - 5 (A)
        - 6 (B)

        Choose a duration for the note to play in milliseconds.
        You can use of the established options below for the DURATION param:
        - 1000 (whole note plays for 1 second)
        - 500 (half note plays for 0.5 seconds)
        - 250 (quarter note plays for 0.25 seconds)

        Alternatively, you can also use a custom duration
        in the range of 0 to 1000 milliseconds.

        Once a musical note starts playing,
        the proceeding command will begin executing immediately.
    """)
    def play_note(self, octave: int, note: int, duration: int = 1000, /):
        """Play musical note."""

    @robotmesh_doc("""
        Play a musical note on the speaker.

        Parameters:
        - note: musical note to play: NoteType enum value
        - octave: octave of the note [1-7], optional
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
    """)
    @act
    def play(self, note: NoteType, octave: int = 3,
             duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC, /):
        """Play musical note."""

    @robotmesh_doc("""
        Play a musical note on the speaker.

        Parameters
        - note: musical note to play: 0=silence/stop, [1-56] numeric value
        - duration: time. 0 to start playing without blocking. Default 0.5
        - timeUnits: of time for the duration. Default sec.
    """)
    @act
    def play_raw(self, note: NoteType,
                 duration: float = 0.5, timeUnits: TimeUnits = TimeUnits.SEC, /):  # noqa: E501
        """Play musical note."""

    @robotmesh_doc("""
        Play the wave sample.

        Parameters:
        - waveType: type of the wave sample sound to play [0..15]
        - waitForCompletion: wait for the sample to finish playing
    """)
    @act
    def play_wave(self, waveType: int, waitForCompletion: bool = True, /):
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
    def play_melody(self, melody: str, /):
        """Play musical melody."""

    @robotmesh_doc("""
        Stop playing music.
    """)
    @act
    def stop(self):
        """Stop sound."""
