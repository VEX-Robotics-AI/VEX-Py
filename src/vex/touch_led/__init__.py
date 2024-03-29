"""Touch LED."""


from collections.abc import Callable, Sequence
from threading import Thread
from typing import LiteralString, Optional, Self

from abm.decor import act, sense

from .._device import Device
from ..brain.port import Ports
from .._common_enums.color import Color

from .._util.doc import robotmesh_doc, vexcode_doc

from .fade import FadeType


__all__: Sequence[LiteralString] = 'Touchled', 'FadeType'


@robotmesh_doc("""
    Use this class when programming with the touch LED device

    Robot Mesh VEX IQ Python B
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_touchled.html
""")
class Touchled(Device):
    """Touch LED."""

    def __init__(self: Self, index: Ports, /):
        """Initialize Touch LED."""
        self.port: Ports = index

        self.fade_type: Optional[FadeType] = None

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @vexcode_doc("""
        Set TouchLED Fade

        Sets how fast the color of an IQ TouchLED fades between colors.

        Choose how fast the TouchLED will fade between colors.
        Replace TYPE with one of the following options:
        - FadeType.SLOW: The TouchLED will slowly fade to a new color.
        - FadeType.FAST: The TouchLED will quickly fade to a new color.
        - FadeType.OFF: The TouchLED will change colors instantly.
    """)
    @act
    def set_fade(self: Self, type: FadeType = FadeType.SLOW, /):
        # pylint: disable=redefined-builtin
        """Set fade type."""
        self.fade_type: FadeType = type

    @robotmesh_doc("""
        Sets the default fade time for the touchled sensor.

        Parameters
        - fadeType: The type of fade the touchled
                    will use: FadeType.SLOW, FAST or OFF
    """)
    @act
    def default_fade(self: Self, fadeType: FadeType, /):
        """Set default fade type."""
        self.fade_type: FadeType = fadeType

    @vexcode_doc("""
        Set TouchLED Brightness

        Sets the brightness of an IQ TouchLED.

        Set TouchLED Brightness accepts
        a range of 0 to 100 for the BRIGHTNESS parameter.
    """)
    @act
    def set_brightness(self: Self, brightness: int = 0, /):
        """Set brightness percentage level."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor, or change current brightness.

        Parameters
        - brightness: brightness for the led 0-100
    """)
    @act
    def brightness(self: Self, brightness: int, /):
        """Set brightness percentage level."""

    @vexcode_doc("""
        Set TouchLED Color

        Sets the color of an IQ TouchLED.

        Replace the COLOR parameter with one of the following options:
        - Color.RED
        - Color.GREEN
        - Color.BLUE
        - Color.WHITE
        - Color.YELLOW
        - Color.ORANGE
        - Color.PURPLE
        - Color.RED_VIOLET
        - Color.VIOLET
        - Color.BLUE_VIOLET
        - Color.BLUE_GREEN
        - Color.YELLOW_GREEN
        - Color.YELLOW_ORANGE
        - Color.RED_ORANGE

        To turn the TouchLED off, set the color to Color.BLACK.
    """)
    @act
    def set_color(self: Self, color: Optional[Color] = None, /):
        """Set color."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters
        - color: color value: 0xRRGGBB
        - brightness: The brightness for the led
    """)
    @act
    def on(self: Self, color: hex, brightness: int = 100, /):
        """Turn on color (hex)."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters
        - colorHue: color of the led: ColorHue enum value
        - brightness: brightness for the led
    """)
    @act
    def on_hue(self: Self, colorHue: Color, brightness: int = 100, /):
        """Turn on color hue."""

    @robotmesh_doc("""
        Turn on the led in the touchled sensor.

        Parameters
        - red: red value of the led, 0-255
        - green: green value of the led, 0-255
        - blue: blue value of the led, 0-255
        - brightness: brightness for the led, 0-100
    """)
    @act
    def on_rgb(self: Self, red: int, green: int, blue: int, brightness: int = 100, /):  # noqa: E501
        """Turn on RGB color."""

    @robotmesh_doc("""
        Turn off the led in the touchled sensor.
    """)
    @act
    def off(self: Self):
        """Turn off LED."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters
        - color: color value: 0xRRGGBB
        - on_time: time the led should remain on in seconds
        - off_time: time the led should remain off in seconds
    """)
    @act
    def blink(self: Self,
              color: hex, on_time: float = 0.25, off_time: float = 0.25, /):
        """Blink color (hex)."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters
        - colorHue: color of the led: ColorHue enum value
        - on_time: time the led should remain on in seconds
        - off_time:  ime the led should remain off in seconds
    """)
    @act
    def blink_hue(self: Self, colorHue: Color,
                  on_time: float = 0.25, off_time: float = 0.25, /):
        """Blink color hue."""

    @robotmesh_doc("""
        Set the led in the touchled sensor as blinking.

        Parameters
        - red: The red value of the led 0-255
        - green: The green value of the led 0-255
        - blue: The blue value of the led 0-255
        - on_time: The time the led should remain on in seconds
        - off_time: The time the led should remain off in seconds
    """)
    @act
    def blink_rgb(self: Self, red: int, green: int, blue: int,
                  on_time: float = 0.25, off_time: float = 0.25, /):
        # pylint: disable=too-many-arguments
        """Blink RGB color."""

    @robotmesh_doc("""
        Get the pressed status of the touchled device.

        Returns True if pressed, False otherwise.
    """)
    @vexcode_doc("""
        TouchLED Pressing

        Reports if a VEX IQ TouchLED is currently being pressed.

        Reports True if the selected TouchLED is being pressed.
        Reports False if the selected TouchLED is not being pressed.
    """)
    @sense
    def pressing(self: Self) -> bool:
        """Return pressed status."""

    @vexcode_doc("""
        TouchLED Pressed

        Runs the specified callback function when an IQ TouchLED is pressed.

        You will need to create a function to call
        when the TouchLED is pressed.
        Provide the name of the function that should run when the event occurs
        as the callback parameter.

        Then, the function is passed
        as the parameter of the TouchLED Pressed function call.

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    def pressed(self: Self, callback: Callable, /):
        """Trigger callback function upon being pressed."""
        def trigger_callback_whenever_pressing():
            while True:
                if self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()

    @vexcode_doc("""
        TouchLED Released

        Runs the specified callback function when an IQ TouchLED is released.

        You will need to create a function to call
        when the TouchLED is released.
        Provide the name of the function that should run
        when the event occurs as the callback parameter.

        Then, the function is passed as the parameter of the TouchLED Released
        function call.

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    def released(self: Self, callback: Callable, /):
        """Trigger callback function upon being released."""
        def trigger_callback_whenever_not_pressing():
            while True:
                if not self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_not_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()
