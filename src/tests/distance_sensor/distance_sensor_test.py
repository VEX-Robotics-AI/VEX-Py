import unittest

from ...vex import Sonar, Ports, MM
from ...testing.io_utils import replace_stdin


class TestSonar(unittest.TestCase):
    def setUp(self):
        self.distance_sensor = Sonar(Ports.PORT1)

    def test_object_distance(self):
        with replace_stdin("""123.4"""):
            self.assertEqual(self.distance_sensor.object_distance(MM), 123.4)


if __name__ == "__main__":
    unittest.main()
