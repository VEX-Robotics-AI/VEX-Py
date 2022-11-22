"""vex.motor.Motor tests."""


import unittest

from ...vex import (
    Motor,
    Ports,
    FORWARD, REVERSE, DEGREES, PERCENT,
)


EXPECTED_VELOCITY = 99


# flake8: noqa
# pylint: disable=missing-class-docstring,missing-function-docstring


class TestMotor(unittest.TestCase):
    def setUp(self):
        self.motor = Motor(Ports.PORT1)

        self.EXPECTED_SPIN_RESULT = (
            "Motor._spin",
            {
                "self": self.motor,
                "direction": REVERSE,
                "velocity": EXPECTED_VELOCITY,
                "unit": PERCENT,
            },
        )

        self.EXPECTED_SPIN_FOR_RESULT = (
            "Motor._spin_for",
            {
                "self": self.motor,
                "direction": FORWARD,
                "rotation": 360,
                "rotation_unit": DEGREES,
                "velocity": EXPECTED_VELOCITY,
                "velocity_unit": PERCENT,
                "wait": True,
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

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT)

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

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT)

    def test_spin_for__without_velocity_param(self):
        self.motor.set_velocity(EXPECTED_VELOCITY, PERCENT)
        result = self.motor.spin_for(
            FORWARD,
            360,
            DEGREES,  # 360 degrees
            True,  # waitForCompletion
        )

        self.assertEqual(result, self.EXPECTED_SPIN_FOR_RESULT)


if __name__ == "__main__":
    unittest.main()
