import unittest
from unittest.mock import Mock
from drivetrain import Drivetrain
from vex import (FORWARD, REVERSE, LEFT, RIGHT)
from vex import (DistanceUnits, BrakeType, PERCENT, MM, DEGREES)


class TestDrivetrain(unittest.TestCase):
    def test_init_happy_path(self):
        motor_left, motor_right = self.__mock_motors()
        dt = Drivetrain(motor_left, motor_right)
        dt = Drivetrain(motor_left, motor_right, 160)
        dt = Drivetrain(motor_left, motor_right, 160, 200)
        dt = Drivetrain(motor_left, motor_right, 160, 200, DistanceUnits.CM)
        dt = Drivetrain(motor_left, motor_right, 160, 200, DistanceUnits.CM, 2.4)

    def test_init_with_empty_constructor_fails(self):
        with self.assertRaises(TypeError):
            dt = Drivetrain()

    def test_drive_forward_happy_path(self):
        dt = self.__create_drivetrain_with_mocked_motors()
        dt.drive(FORWARD, 10, PERCENT)
        dt.drive(FORWARD, 10)

    def test_can_call_all_methods_happy_path(self):
        dt = self.__create_drivetrain_with_mocked_motors()
        dt.drive_for(FORWARD, 10, MM, 20, PERCENT)
        dt.start_drive_for(REVERSE, 10, MM, 20, PERCENT)
        dt.turn(LEFT, 10, PERCENT)
        dt.turn_for(RIGHT, 90, DEGREES, 10, PERCENT)
        dt.start_turn_for(RIGHT, 90, DEGREES, 10, PERCENT)
        dt.arcade(50, 30)
        dt.stop()
        dt.set_gear_ratio(2.4)
        dt.set_drive_velocity(10, PERCENT)
        dt.set_turn_velocity(10, PERCENT)
        dt.set_timeout(2)
        dt.timeout()
        dt.did_timeout()
        dt.is_done()
        dt.set_stopping(BrakeType.BRAKE)
        dt.velocity()
        dt.current()

    def __create_drivetrain_with_mocked_motors(self):
        motor_left, motor_right = self.__mock_motors()
        return Drivetrain(motor_left, motor_right)

    def __mock_motors(self):
        motor_left = Mock()
        motor_right = Mock()
        return motor_left, motor_right


if __name__ == '__main__':
    unittest.main()
