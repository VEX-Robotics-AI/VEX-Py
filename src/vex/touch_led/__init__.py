"""VEX Touch LED."""


from collections.abc import Sequence

from abm.decor import act, sense

from .._abstract import Device
from ..color_sensor import ColorHue
from ..port import Ports

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from .fade_type import FadeType


__all__: Sequence[str] = 'Touchled', 'FadeType'


@robotmesh_doc("""
    Use this class when programming with the touch LED device.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_touchled.html
""")
class Touchled(Device):
    """Touch LED."""

    def __init__(self, index: Ports):
        """Initialize Touch LED."""
        self.port: Ports = index

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Set the default fade time for the touchled sensor.

        Parameters:
        - fadeType: The type of fade the touchled
                    will use: FadeType.SLOW, FAST or OFF
    """)
    @act
    def default_fade(self, fadeType: FadeType):
        """Set default Fade Type."""
        # pylint: disable=attribute-defined-outside-init
        self.fade_type: FadeType = fadeType

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
    def on(self, color: hex, brightness: int = 100):
        """Turn on color."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters:
        - colorHue: The color of the led: ColorHue enum value
        - brightness: The brightness for the led
    """)
    @act
    def on_hue(self, colorHue: ColorHue, brightness: int = 100):
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
    def on_rgb(self, red: int, green: int, blue: int, brightness: int = 100):
        """Turn on RGB color."""

    @robotmesh_doc("""
        Turn off the led in the touchled sensor.
    """)
    @act
    def off(self):
        """Turn off LED."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor, or change current brightness.

        Parameters:
        - brightness: The brightness for the led 0-100
    """)
    @act
    def brightness(self, brightness: int):
        """Set Brightness Percent Level."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters:
        - color: color value: 0xRRGGBB
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """)
    @act
    def blink(self, color: hex, on_time: float = 0.25, off_time: float = 0.25):
        """Blink color."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters:
        - colorHue: The color of the led: ColorHue enum value
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """)
    @act
    def blink_hue(
            self, colorHue: ColorHue,
            on_time: float = 0.25, off_time: float = 0.25):
        """Blink Color Hue."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters:
        - red: The red value of the led 0-255
        - green: The green value of the led 0-255
        - blue: The blue value of the led 0-255
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """)
    @act
    def blink_rgb(   # pylint: disable=too-many-arguments
            self, red: int, green: int, blue: int,
            on_time: float = 0.25, off_time: float = 0.25):
        """Blink RGB Color."""
