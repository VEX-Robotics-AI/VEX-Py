import unittest

from ...vex import Motor
from ...vex import FORWARD, REVERSE, DEGREES, PERCENT, FORWARD, Ports

EXPECTED_VELOCITY = 99


class TestMotor(unittest.TestCase):
    def setUp(self):
        self.motor = Motor(Ports.PORT1, False)
        self.EXPECTED_SPIN_RESULT = (
            "Motor._spin",
            {
                "dir": REVERSE,
                "self": self.motor,
                "velocity": EXPECTED_VELOCITY,
                "velocityUnits": PERCENT,
            },
        )
        self.EXPECTED_SPIN_FOR_RESULT_TUPLE = (
            "Motor._spin_for",
            {
                "dir": FORWARD,
                "rotation": 360,
                "rotationUnits": DEGREES,
                "self": self.motor,
                "velocity": EXPECTED_VELOCITY,
                "velocityUnits": PERCENT,
                "waitForCompletion": True,
            },
        )

    def test_spin(self):
        result = self.motor.spin(REVERSE, EXPECTED_VELOCITY)

        self.assertEqual(result, self.EXPECTED_SPIN_RESULT)

    def test_spin__without_velocity_param(self):
        self.motor.set_velocity(EXPECTED_VELOCITY)
        result = self.motor.spin(REVERSE)

        self.assertEqual(result, self.EXPECTED_SPIN_RESULT)

    def test_spin_for(self):
        result = self.motor.spin_for(
            FORWARD,
            360,
            DEGREES,  # 360 degrees
            EXPECTED_VELOCITY,
            PERCENT,
            True,  # waitForCompletion
        )

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT_TUPLE)

    def test_spin_for__with_velocity_is_none(self):
        self.motor.set_velocity(EXPECTED_VELOCITY, PERCENT)
        result = self.motor.spin_for(
            FORWARD,
            360,
            DEGREES,  # 360 degrees
            None,  # velocity
            PERCENT,
            True,  # waitForCompletion
        )

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT_TUPLE)

    def test_spin_for__without_velocity_param(self):
        self.motor.set_velocity(EXPECTED_VELOCITY, PERCENT)
        result = self.motor.spin_for(
            FORWARD,
            360,
            DEGREES,  # 360 degrees
            True,  # waitForCompletion
        )

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT_TUPLE)


if __name__ == "__main__":
    unittest.main()
