import unittest

from ...vex import Touchled, FadeType, Ports


class TestTouchLed(unittest.TestCase):
    def setUp(self):
        self.touch_led = Touchled(Ports.PORT1)

    def test_touch_led_set_fade(self):
        self.touch_led.set_fade(FadeType.OFF)
        self.touch_led.set_fade(FadeType.SLOW)
        self.touch_led.set_fade(FadeType.FAST)


if __name__ == "__main__":
    unittest.main()
