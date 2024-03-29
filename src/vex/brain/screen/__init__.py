"""Brain LCD Screen."""


from collections.abc import Sequence
from typing import LiteralString, Optional, Self

from abm.decor import act

from ..._device import SingletonDevice
from ..._common_enums.color import Color

from ..._util.doc import robotmesh_doc, vexcode_doc

from .font import (
    Font,
    MONO_M, MONO_L, MONO_XL, MONO_XXL, MONO_S, MONO_XS,
    PROP_M, PROP_L, PROP_XL, PROP_XXL,
    FontType)


__all__: Sequence[LiteralString] = (
    'BrainLcd',
    'Font',
    'MONO_M', 'MONO_L', 'MONO_XL', 'MONO_XXL', 'MONO_S', 'MONO_XS',
    'PROP_M', 'PROP_L', 'PROP_XL', 'PROP_XXL',
    'FontType')


@robotmesh_doc("""
    Use this class to write or draw to the brain's LCD screen.

    * 21 characters wide
    * 5 lines (1-5)

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain_lcd.html
""")
class BrainLcd(SingletonDevice):
    """Brain LCD Screen."""

    def __init__(self: Self):
        """Initialize Brain LCD Screen."""
        self.font: FontType = FontType.MONO20

        self.pen_width: int = 1

        self.pen_color: Color = Color.WHITE

        self.fill_color: Color = Color.BLACK

    @vexcode_doc("""
        Brain Screen Set Font

        Sets the style and size of font used on the IQ (2nd generation) Brain's
        screen when printing numbers or text.

        There are two different types of fonts available on the IQ
        (2nd generation) Brain's screen:
        - Monospaced (Mono): each character takes up the same width.
        - Proportional (Prop): each character takes up different size widths
          based on the character.

        Choose which font type and size to use. You can replace the FONT
        parameter with one of the following font options:
        - FontType.MONO12
        - FontType.MONO15
        - FontType.MONO20
        - FontType.MONO30
        - FontType.MONO40
        - FontType.MONO60
        - FontType.PROP20
        - FontType.PROP30
        - FontType.PROP40
        - FontType.PROP60

        The new font size will be used for any future text written to
        the IQ (2nd generation) Brain's screen.
    """)
    @act
    def set_font(self: Self, fontname: FontType, /):
        """Set font style & size."""
        self.font: FontType = fontname

    @vexcode_doc("""
        Brain Screen Set Pen Width

        Sets the width of the outline for shapes drawn on
        the IQ (2nd generation) Brain's screen.

        The Brain Screen Set Pen Width command is used to set the width
        of the line on the outside of circles and rectangles drawn on
        the IQ (2nd generation) Brain's screen.

        It accepts integer values for the WIDTH parameter, with a larger value
        equating to a larger width.
    """)
    @act
    def set_pen_width(self: Self, width: int, /):
        """Set the width of the outline for shapes drawn on brain's screen."""
        self.pen_width: int = width

    @vexcode_doc("""
        Brain Screen Set Pen Color

        Sets color of lines drawn on IQ (2nd generation) Brain's screen.

        The Brain Screen Set Pen Color command is used to set the color of
        lines, pixels and text drawn on the IQ (2nd generation) Brain's screen.

        It can also be used to set the color the outline of
        circles and rectangles drawn on the IQ (2nd generation) Brain's screen.

        You can replace the COLOR parameter with one of the following options:
        - Color.BLACK
        - Color.BLUE
        - Color.BLUE_GREEN
        - Color.BLUE_VIOLET
        - Color.GREEN
        - Color.ORANGE
        - Color.PURPLE
        - Color.RED
        - Color.RED_ORANGE
        - Color.RED_VIOLET
        - Color.VIOLET
        - Color.WHITE
        - Color.YELLOW
        - Color.YELLOW_GREEN
        - Color.YELLOW_ORANGE

        The pen color will be used for any next objects drawn
        on the IQ (2nd generation) Brain's screen.
    """)
    @act
    def set_pen_color(self: Self, color: Color, /):
        """Set drawing-pen color."""
        self.pen_color: Color = color

    @vexcode_doc("""
        Brain Screen Set Fill Color

        Sets the color that fills in shapes drawn on the Brain's screen.

        The Brain Screen Set Fill Color command is used to set the color of the
        inside of circles and rectangles drawn on the Brain's screen.

        You can replace the COLOR parameter with one of the following options:
        - Color.BLACK
        - Color.BLUE
        - Color.BLUE_GREEN
        - Color.BLUE_VIOLET
        - Color.GREEN
        - Color.ORANGE
        - Color.PURPLE
        - Color.RED
        - Color.RED_ORANGE
        - Color.RED_VIOLET
        - Color.VIOLET
        - Color.WHITE
        - Color.YELLOW
        - Color.YELLOW_GREEN
        - Color.YELLOW_ORANGE

        The fill color will be used for any next objects drawn
        on the IQ (2nd generation) Brain's screen.
    """)
    @act
    def set_fill_color(self: Self, color: Color, /):
        """Set shape-filling color."""
        self.fill_color: Color = color

    @vexcode_doc("""
        Print

        Prints values or text on the IQ Brain's screen.

        The Print command will print data at a cursor location on the screen.

        All new projects begin with the screen cursor at row 1 column 1.

        - Print words and numbers:
            brain.screen.print("Number:", 10)

        - Print the reported value from a variable:
            brain.screen.print(variable)

        - Print the reported value from a sensor or device:
            brain.screen.print(drivetrain.is_done())
    """)
    @act
    def print(self: Self, *args):
        """Print numerical values and/or text strings on Brain LCD Screen."""

    @robotmesh_doc("""
        Prints a number, string, or boolean at a particular line,
        clearing the rest of the line

        Parameters
        number: Line to print on, 1 is top line.
        text: object to print, usually a string.
              Use "" to clear the line.
              For multiple arguments, use format like
              "x: %g y: %g" % (x, y) -> "x: 123 y: 456"
              Supported format flags are g (all) x (hex) d (int) f (float)
    """)
    @act
    def print_line(self: Self, number: int, text: str, /):
        """Print given text to specified line."""

    @vexcode_doc("""
        Set Cursor

        Sets the cursor location for Brain's Print commands.

        The Set Cursor command requires 2 parameters:
        - ROW: Screen row position
        - COL: Screen column position

        Set the cursor's row and column position to have a Print command
        print at a specific location on the screen.

        The IQ (2nd generation) Brain allows you to change the size of the font
        printed on the screen. Changing the font will affect the number of rows
        and columns available on the Brain's screen.

        Accepts a range for ROW of 1 to 9.
        Accepts a range for COL of 1 to 28.
    """)
    @act
    def set_cursor(self: Self, row: int, col: int, /):
        """Set cursor location."""

    @vexcode_doc("""
        New Line

        Sets the print output cursor on the IQ Brain's screen
        to the next available row.

        By default, all projects begin with the screen cursor
        at row 1 column 1. The New Line command will move the cursor
        down by a single row on the screen.

        The IQ (2nd generation) Brain allows you to change the size of the font
        printed on the screen. Changing the font will affect the number of rows
        and columns available on the Brain's screen.
    """)
    @act
    def next_row(self: Self):
        """Move cursor to new line."""

    @robotmesh_doc("""
        Clears the whole screen.
    """)
    @vexcode_doc("""
        Clear Screen

        Clears the entire VEX IQ Brain's Screen.

        Clear Screen will not reset the Brain's screen cursor.

        Use the Set Cursor command to set the Brain's cursor
        to the desired position.
    """)
    @act
    def clear_screen(self: Self):
        """Clear entire screen."""

    @vexcode_doc("""
        Clear Line

        Clears the current row on the VEX IQ Brain's Screen.

        Clears a specified row on the VEX IQ Brain's screen.

        You can call the Clear Line command without any arguments
        to clear the current row.
    """)
    @act
    def clear_row(self: Self, row: Optional[int] = None, /):
        """Clear specified row or current row."""

    @vexcode_doc("""
        Brain Screen Draw Pixel

        Draws a pixel on the IQ (2nd generation) Brain's screen.

        The Brain Screen Draw Pixel command requires 2 values:
        - X: X coordinate
        - Y: Y coordinate

        The pixel color is determined by the Brain's Set Pen Color command.
        The default pixel color is white.
    """)
    @act
    def draw_pixel(self: Self, x: int, y: int):
        """Draw pixel."""

    @vexcode_doc("""
        Brain Screen Draw Line

        Draws a line on the IQ (2nd generation) Brain's screen.

        The Brain Screen Draw Line command requires 4 values:
        - START_X: Beginning X coordinate
        - START_Y: Beginning Y coordinate
        - END_X: Ending X coordinate
        - END_Y: Ending Y coordinate

        The line color is determined by the Brain's Set Pen Color command.
        The default line color is white.
    """)
    @act
    def draw_line(self: Self, x1: int, y1: int, x2: int, y2: int):
        """Draw line."""

    @vexcode_doc("""
        Brain Screen Draw Rectangle

        Draws a rectangle on the IQ (2nd generation) Brain's screen.

        The Brain Screen Draw Rectangle command requires 4 values:
        - X: Top Left Corner X coordinate
        - Y: Top Left Corner Y coordinate
        - WIDTH: Width of the rectangle
        - HEIGHT: Height of the rectangle

        The outside line color of the rectangle is determined
        by the Brain's Set Pen Color command. The default line color is white.

        The inside fill color of the rectangle is determined
        by the Brain's Set Fill Color command. The default fill color is black.
    """)
    @act
    def draw_rectangle(self: Self, x: int, y: int, width: int, height: int):
        """Draw rectangle."""

    @vexcode_doc("""
        Brain Screen Draw Circle

        Draws a circle on the IQ (2nd generation) Brain's screen.

        The Brain Screen Draw Circle command requires 3 values:
        - X: X coordinate of the circle's center
        - Y: Y coordinate of the circle's center
        - RADIUS: Radius of circle (in pixels)

        The outside line color of the circle is determined by the Brain's
        Set Pen Color command. The default line color is white.

        The inside fill color of the circle is determined by the Brain's
        Set Fill Color command. The default fill color is black.
    """)
    @act
    def draw_circle(self: Self, x: int, y: int, radius: int):
        """Draw circle."""
