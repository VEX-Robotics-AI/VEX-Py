import unittest

from vex import Brain, NoteType, SECONDS


class TestBrainSound(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_sound_dot_play(self):
        self.brain.sound.play(
            NoteType.F,  # note
            4,  # octave
            0.5,  # time duration
            SECONDS,  # time unit
        )

    def test_play_sound(self):
        self.brain.play_sound(NoteType.F)

    def test_play_note(self):
        self.brain.play_note(
            4,  # octave
            4,  # G note
            1000,  # ms
        )


if __name__ == "__main__":
    unittest.main()
