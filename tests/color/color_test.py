import unittest

from vex import ColorSensor, ColorHue, Ports
from ..io_utils import replace_stdin


class TestColorSensor(unittest.TestCase):
    def setUp(self):
        self.colorSensor = ColorSensor(Ports.PORT1)

    def test_is_near_object(self):
        with replace_stdin("""0"""):
            self.assertEqual(self.colorSensor.is_near_object(), False)

    def test_color(self):
        with replace_stdin("""1"""):
            self.assertEqual(self.colorSensor.color(), ColorHue.RED)

    def test_brightness(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.colorSensor.brightness(), 1234)

    def test_hue(self):
        with replace_stdin("""200"""):
            self.assertEqual(self.colorSensor.hue(), 200)

if __name__ == "__main__":
    unittest.main()

