import unittest

from ...vex import Gyro, GyroCalibrationType, DEGREES, Ports
from ...testing.io_utils import replace_stdin


class TestGyroSensor(unittest.TestCase):
    def setUp(self):
        self.gyro = Gyro(Ports.PORT2)

    def test_calibrate(self):
        self.gyro.calibrate(GyroCalibrationType.NORMAL)

    def test_set_heading(self):
        self.gyro.set_heading(0, "DEGREES")

    def test_set_rotation(self):
        self.gyro.set_rotation(0, "DEGREES")

    def test_heading(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.gyro.heading(DEGREES), 1234)

    def test_rotation(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.gyro.heading(DEGREES), 1234)

    def test_rate(self):
        with replace_stdin("""1234"""):
            self.assertEqual(self.gyro.rate(), 1234)


if __name__ == "__main__":
    unittest.main()
