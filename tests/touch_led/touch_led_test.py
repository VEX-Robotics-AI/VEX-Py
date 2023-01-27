import unittest

from vex import Touchled, FadeType, Ports, ColorHue


class TestTouchLed(unittest.TestCase):
    def setUp(self):
        self.touch_led = Touchled(Ports.PORT1)

    def test_touch_led_set_fade(self):
        self.touch_led.set_fade(FadeType.OFF)
        self.touch_led.set_fade(FadeType.SLOW)
        self.touch_led.set_fade(FadeType.FAST)

    def test_touch_led_set_color(self):
        self.touch_led.set_color(ColorHue.RED)

    def test_touch_led_set_brightness(self):
        self.touch_led.set_brightness(25)


if __name__ == "__main__":
    unittest.main()
