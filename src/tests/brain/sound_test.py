import unittest

from ...vex import (
    Brain,
    NoteType, SECONDS
)


class TestBrainSound(unittest.TestCase):

    def setUp(self):
        self.brain = Brain()

    def test_play_sound(self):
        self.brain.sound.play(
            NoteType.F,  # note
            4,  # octave
            0.5,  # time duration
            SECONDS,  # time unit
        )


if __name__ == '__main__':
    unittest.main()
