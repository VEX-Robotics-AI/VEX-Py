"""Touch LED."""


from collections.abc import Sequence
from typing import Optional

from abm.decor import act, sense

from .._abstract_device import Device
from ..color_sensor import ColorHue
from ..brain.port import Ports
from ..util.doc import robotmesh_doc, vexcode_doc
from .color import Color
from .fade_type import FadeType


__all__: Sequence[str] = 'Touchled', 'Color', 'FadeType'


@robotmesh_doc("""
    Use this class when programming with the touch LED device.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_touchled.html
""")
class Touchled(Device):
    """Touch LED."""

    def __init__(self, index: Ports):
        """Initialize Touch LED."""
        self.port: Ports = index

        self.default_fade_type: Optional[FadeType] = None

    def __hash__(self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Set the default fade time for the touchled sensor.

        Parameters:
        - fadeType: The type of fade the touchled
                    will use: FadeType.SLOW, FAST or OFF
    """)
    @act
    def default_fade(self, fadeType: FadeType, /):
        """Set default fade type."""
        self.default_fade_type: FadeType = fadeType

    @robotmesh_doc("""
        Get the pressed status of the touchled device.

        Returns:
        True if pressed, False otherwise
    """)
    @sense
    def pressing(self) -> bool:
        """Return Touch LED's pressed status."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters:
        - color: color value: 0xRRGGBB
        - brightness: The brightness for the led
    """)
    @act
    def on(self, color: hex, brightness: int = 100, /):
        """Turn on color."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters:
        - colorHue: The color of the led: ColorHue enum value
        - brightness: The brightness for the led
    """)
    @act
    def on_hue(self, colorHue: ColorHue, brightness: int = 100, /):
        """Turn on Color Hue."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters:
        - red: The red value of the led, 0-255
        - green: The green value of the led, 0-255
        - blue: The blue value of the led, 0-255
        - brightness: The brightness for the led, 0-100
    """)
    @act
    def on_rgb(self, red: int, green: int, blue: int, brightness: int = 100, /):  # noqa: E501
        """Turn on RGB color."""

    @robotmesh_doc("""
        Turn off the led in the touchled sensor.
    """)
    @act
    def off(self):
        """Turn off LED."""

    @vexcode_doc("""
        Set fade time for the touchled sensor.

        Parameters:
        - fadeType: The type of fade the touchled
                    will use: FadeType.SLOW, FAST or OFF
    """)
    @act
    def set_fade(self, fadeType: FadeType, /):
        """Set default Fade Type."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor, or change current brightness.

        Parameters:
        - brightness: The brightness for the led 0-100
    """)
    @act
    def brightness(self, brightness: int, /):
        """Set Brightness Percent Level."""

    @robotmesh_doc(
        """
        Set the led in the touchled sensor as blinking.

        Parameters:
        - color: color value: 0xRRGGBB
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """
    )
    @act
    def blink(
        self, color: hex, on_time: float = 0.25, off_time: float = 0.25, /
    ):  # noqa: E501
        """Blink color."""

    @robotmesh_doc(
        """
        Set the led in the touchled sensor as blinking.

        Parameters:
        - colorHue: The color of the led: ColorHue enum value
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """
    )
    @act
    def blink_hue(
        self, colorHue: ColorHue, on_time: float = 0.25, off_time: float = 0.25, /
    ):
        """Blink Color Hue."""

    @robotmesh_doc(
        """
        Set the led in the touchled sensor as blinking.

        Parameters:
        - red: The red value of the led 0-255
        - green: The green value of the led 0-255
        - blue: The blue value of the led 0-255
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """
    )
    @act
    def blink_rgb(  # pylint: disable=too-many-arguments
        self,
        red: int,
        green: int,
        blue: int,
        on_time: float = 0.25,
        off_time: float = 0.25,
        /,
    ):
        """Blink RGB Color."""

    @act
    @vexcode_doc(
        """
        Set TouchLED Brightness
            Sets the brightness of an IQ TouchLED.

            touchled.set_brightness(BRIGHTNESS)
        
        How To Use
            Set TouchLED Brightness accepts a range of 0 to 100 for the BRIGHTNESS parameter.

            touchled.set_brightness(50)
        
        Example
            This example will illuminate the TouchLED at 25 percent brightness.

            touchled.set_brightness(25)
    """
    )
    def set_brightness(self, brightness: int, /):
        """Set Brightness Percent Level."""

    @vexcode_doc("""
        Defined color values.
    """)
    @act
    def default_color(self, color: Color, /):
        """Set default Fade Type."""
        
        self.color: Color = color

    @vexcode_doc(
        """
        Set TouchLED Color
        Sets the color of an IQ TouchLED.
            touchled.set_color(COLOR)

        How To Use
        Replace the COLOR parameter with one of the following options:

            Color.RED
            Color.GREEN
            Color.BLUE
            Color.WHITE
            Color.YELLOW
            Color.ORANGE
            Color.PURPLE
            Color.RED_VIOLET
            Color.VIOLET
            Color.BLUE_VIOLET
            Color.BLUE_GREEN
            Color.YELLOW_GREEN
            Color.YELLOW_ORANGE
            Color.RED_ORANGE

        To turn the TouchLED off, set the color to Color.BLACK.

        touchled.set_color(Color.BLACK)
        """

    )
    def set_color(self, color: Color):
        """Set the color of an IQ TouchLED."""
