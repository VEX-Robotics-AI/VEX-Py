import unittest

from ...vex import Controller


def callback_func():
    print("Button pressed")

class testL3AndR3Buttons(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
    def L3_is_pressed(self):
        self.controller.buttonL3.pressed(callback_func)
    def R3_is_pressed(self):
        self.controller.butoonR3.pressed(callback_func)

if __name__ == "__main__":
    unittest.main()


