import unittest

#import both Bumper and bumper_switch_sensor does not work
#from ...vex import ColorHue
from ...vex import Bumper, Ports


def callback_func():
    print("Button pressed/released")

   
class testBumperSwitchSensor(unittest.TestCase):
    def setUp(self):
        self.bumper = Bumper(Ports.PORT1)

    def test_bumper_is_pressed(self):
        self.bumper.pressed(callback_func)

    def test_bumper_is_released(self):
        self.bumper.released(callback_func)


if __name__ == "__main__":
    unittest.main()