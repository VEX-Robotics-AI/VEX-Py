import unittest

from ...vex import Inertial
from ...vex import DEGREES, VelocityUnits
from ...vex._common_enums.axis import XAXIS, YAXIS, ZAXIS
from ...vex._common_enums.orientation import PITCH, ROLL, YAW
from ...testing.io_utils import replace_stdin


class TestInertialSensor(unittest.TestCase):
    def setUp(self):
        self.inertial = Inertial()

    def test_inertial_calibrate(self):
        self.inertial.calibrate()

    def test_set_heading(self):
        self.inertial.set_heading(12.3, DEGREES)

    def test_set_rotation(self):
        self.inertial.set_rotation(12.3, DEGREES)

    def test_heading(self):
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.heading(DEGREES), 32.1)

    def test_rotation(self):
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.rotation(DEGREES), 32.1)

    def test_acceleration(self):
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.acceleration(XAXIS), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.acceleration(YAXIS), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.acceleration(ZAXIS), 32.1)

    def test_gyro_rate(self):
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.gyro_rate(XAXIS, VelocityUnits.DPS), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.gyro_rate(YAXIS, VelocityUnits.DPS), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.gyro_rate(ZAXIS, VelocityUnits.DPS), 32.1)

    def test_orientation(self):
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.orientation(PITCH, DEGREES), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.orientation(ROLL, DEGREES), 32.1)
        with replace_stdin("""32.1"""):
            self.assertEqual(self.inertial.orientation(YAW, DEGREES), 32.1)


if __name__ == "__main__":
    unittest.main()
