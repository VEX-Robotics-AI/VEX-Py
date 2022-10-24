import unittest

from ...vex import Brain, SECONDS
from ...testing.io_utils import replace_stdin


class TestBrainTimmer(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_brain_timmer_clear(self):
        self.brain.timer.clear()

    def test_brain_timer_time(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.brain.timer.time(SECONDS), 1234)


if __name__ == "__main__":
    unittest.main()
