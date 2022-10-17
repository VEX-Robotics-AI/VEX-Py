import unittest

from ...vex import Brain


class TestBrainScreen(unittest.TestCase):

    def setUp(self):
        self.brain = Brain()

    def test_print_line(self):
        self.brain.screen.print_line(2, 'Hello World')


if __name__ == '__main__':
    unittest.main()
