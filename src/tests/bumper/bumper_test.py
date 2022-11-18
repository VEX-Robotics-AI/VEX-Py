import unittest

#import both Bumper and bumper_switch_sensor does not work
from ...vex import ColorHue
#from ...vex import Bumper


def callback_func():
    print("Button pressed")

   
class testBumperSwitchSensor(unittest.TestCase):
    def setUp(self):
        self.bumper = Bumper()
    def test_bumper_is_pressed(self):
        self.bumper.pressed(callback_func)


if __name__ == "__main__":
    unittest.main()
