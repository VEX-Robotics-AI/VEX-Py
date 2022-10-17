import unittest

from ...vex import Brain


class TestBrainScreen(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_print_line(self):
        self.brain.screen.print_line(2, "Hello World")

    def test_screen_clear_screen(self):
        self.brain.screen.clear_screen()

    def test_screen_set_cursor(self):
        self.brain.screen.set_cursor(1, 1)


if __name__ == "__main__":
    unittest.main()
