import unittest

from vex import DriveTrain
from vex import Motor, Ports, DEGREES, PERCENT, FORWARD, REVERSE, MM, LEFT, CurrentUnits
from ..testing.io_utils import replace_stdin


class TestDriveTrain(unittest.TestCase):
    def setUp(self):
        self.drivetrain = DriveTrain(
            Motor(Ports.PORT1),  # left_motor
            [  # right_motor
                Motor(Ports.PORT2),
                Motor(Ports.PORT3)
            ],
        )

    def test_drive(self):
        self.drivetrain.drive(FORWARD)

    def test_drive_for(self):
        self.drivetrain.drive_for(REVERSE, 12.3),
        self.drivetrain.drive_for(REVERSE, 12.3, MM, True)

    def test_turn(self):
        self.drivetrain.turn(LEFT)

    def test_turn_for(self):
        self.drivetrain.turn_for(LEFT, 12.3, DEGREES),
        self.drivetrain.turn_for(LEFT, 12.3, DEGREES, True)

    # def test_turn_to_heading(self):
    #     self.assertEqual(
    #         self.drivetrain.turn_to_heading(12.3),
    #         self.drivetrain.turn_to_heading(12.3, DEGREES)
    #     )

    # def test_turn_to_rotation(self):
    #     self.assertEqual(
    #         self.drivetrain.turn_to_rotation(12.3),
    #         self.drivetrain.turn_to_rotation(12.3, DEGREES),
    #     )

    # def test_set_heading(self):
    #     self.assertEqual(
    #         self.drivetrain.set_heading(12.3),
    #         self.drivetrain.set_heading(12.3, DEGREES)
    #     )

    # def test_set_rotation(self):
    #     self.assertEqual(
    #         self.drivetrain.set_rotation(12.3),
    #         self.drivetrain.set_rotation(12.3, DEGREES)
    #     )

    def test_is_moving(self):
        with replace_stdin("0"):
            self.assertEqual(self.drivetrain.is_moving(), False)
        with replace_stdin("1"):
            self.assertEqual(self.drivetrain.is_moving(), True)

    # def test_heading(self):
    #     with replace_stdin("34.5"):
    #         self.assertEqual(self.drivetrain.heading(), 34.5)
    #     with replace_stdin("34.5"):
    #         self.assertEqual(self.drivetrain.heading(DEGREES), 34.5)

    # def test_rotation(self):
    #     with replace_stdin("34.5"):
    #         self.assertEqual(self.drivetrain.rotation(), 34.5)
    #     with replace_stdin("34.5"):
    #         self.assertEqual(self.drivetrain.rotation(DEGREES), 34.5)

    def test_velocity(self):
        with replace_stdin("34.5"):
            self.assertEqual(self.drivetrain.velocity(), 34.5)
        with replace_stdin("34.5"):
            self.assertEqual(self.drivetrain.velocity(PERCENT), 34.5)

    def test_current(self):
        with replace_stdin("34.5"):
            self.assertEqual(self.drivetrain.current(), 34.5)
        with replace_stdin("34.5"):
            self.assertEqual(self.drivetrain.current(CurrentUnits.AMP), 34.5)


if __name__ == "__main__":
    unittest.main()
