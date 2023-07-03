import unittest

from vex import Distance, ObjectSizeType, Ports, MM
from vex_util.io import replace_stdin


class TestDistanceSensor(unittest.TestCase):
    def setUp(self):
        self.distance_sensor = Distance(Ports.PORT1)

    def test_object_distance(self):
        with replace_stdin("123.4"):
            self.assertEqual(self.distance_sensor.object_distance(MM), 123.4)

    def test_object_velocity(self):
        with replace_stdin("123.4"):
            self.assertEqual(self.distance_sensor.object_velocity(), 123.4)

    def test_object_size(self):
        with replace_stdin("1"):
            self.assertEqual(self.distance_sensor.object_size(), ObjectSizeType.SMALL)
        with replace_stdin("2"):
            self.assertEqual(self.distance_sensor.object_size(), ObjectSizeType.MEDIUM)
        with replace_stdin("3"):
            self.assertEqual(self.distance_sensor.object_size(), ObjectSizeType.LARGE)

    def test_is_object_detected(self):
        with replace_stdin("0"):
            self.assertEqual(self.distance_sensor.is_object_detected(), False)
        with replace_stdin("1"):
            self.assertEqual(self.distance_sensor.is_object_detected(), True)


if __name__ == "__main__":
    unittest.main()
