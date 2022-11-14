import unittest

from ...vex import Brain
from ...testing.io_utils import replace_stdin


class TestBrainBattery(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_battery_capacity(self):
        with replace_stdin('100'):
            self.assertEqual(self.brain.battery.capacity(), 100)


if __name__ == "__main__":
    unittest.main()
