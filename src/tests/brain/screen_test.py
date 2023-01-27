import unittest

from vex import Brain, ColorHue


class TestBrainScreen(unittest.TestCase):
    def setUp(self):
        self.brain = Brain()

    def test_print_line(self):
        self.brain.screen.print_line(2, "Hello World")

    def test_screen_clear_screen(self):
        self.brain.screen.clear_screen()

    def test_screen_set_cursor(self):
        self.brain.screen.set_cursor(1, 1)

    def test_print(self):
        self.brain.screen.print("VEXCode")
        # TODO: enables the test below when @act supports *params.
        # self.brain.screen.print("Number: ", 10)

    def test_next_row(self):
        self.brain.screen.next_row()

    def test_clear_row(self):
        self.brain.screen.clear_row(1)

    def test_draw_pixel(self):
        self.brain.screen.draw_pixel(0, 0)

    def test_draw_line(self):
        self.brain.screen.draw_line(0, 0, 10, 10)

    def test_draw_rectangle(self):
        self.brain.screen.draw_rectangle(0, 0, 10, 10)

    def test_draw_circle(self):
        self.brain.screen.draw_circle(0, 0, 10)

    def test_set_font(self):
        self.brain.screen.set_font(20)

    def test_set_pen_width(self):
        self.brain.screen.set_pen_width(10)

    def test_set_pen_color(self):
        self.brain.screen.set_pen_color(ColorHue.RED)

    def test_set_fill_color(self):
        self.brain.screen.set_fill_color(ColorHue.RED)


if __name__ == "__main__":
    unittest.main()
