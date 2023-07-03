import unittest

from vex import (
    Optical, Ports,
    LedStateType, GestureType, ColorHue,
    PERCENT,
)
from vex._util.io import replace_stdin


def callback_func():
    print("1234")


class TestOpticalSensor(unittest.TestCase):
    def setUp(self):
        self.optical = Optical(Ports.PORT1)

    def test_act_methods(self):
        self.optical.gesture_enable()
        self.optical.gesture_disable()
        self.optical.set_light(LedStateType.ON)
        self.optical.set_light_power(123)
        self.optical.set_light_power(123, PERCENT)

    def test_act_callback_methods(self):
        self.optical.object_detected(callback_func)
        self.optical.object_lost(callback_func)
        self.optical.gesture_up(callback_func)
        self.optical.gesture_down(callback_func)
        self.optical.gesture_left(callback_func)
        self.optical.gesture_right(callback_func)

    def test_get_gesture(self):
        with replace_stdin("""1"""):
            self.assertEqual(self.optical.get_gesture(), GestureType.UP)
        with replace_stdin("""2"""):
            self.assertEqual(self.optical.get_gesture(), GestureType.DOWN)
        with replace_stdin("""3"""):
            self.assertEqual(self.optical.get_gesture(), GestureType.LEFT)
        with replace_stdin("""4"""):
            self.assertEqual(self.optical.get_gesture(), GestureType.RIGHT)

    def test_is_near_object(self):
        with replace_stdin("""0"""):
            self.assertFalse(self.optical.is_near_object())
        with replace_stdin("""1"""):
            self.assertTrue(self.optical.is_near_object())

    def test_color(self):
        with replace_stdin("""1"""):
            self.assertEqual(self.optical.color(), ColorHue.RED)

    def test_brightness(self):
        with replace_stdin("""33"""):
            self.assertEqual(self.optical.brightness(), 33)

    def test_hue(self):
        with replace_stdin("""33"""):
            self.assertEqual(self.optical.hue(), 33)


if __name__ == "__main__":
    unittest.main()
