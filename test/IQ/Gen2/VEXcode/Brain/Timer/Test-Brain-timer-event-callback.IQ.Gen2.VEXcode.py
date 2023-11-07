import unittest

from vex import Brain, SECONDS
from vex._util.io import replace_stdin


class TestBrainTimer(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_brain_timer_clear(self):
        self.brain.timer.clear()

    def test_brain_timer_time(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.brain.timer.time(SECONDS), 1234)


if __name__ == "__main__":
    unittest.main()
