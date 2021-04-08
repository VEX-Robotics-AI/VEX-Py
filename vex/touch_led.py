from enum import IntEnum

from __decor import act, sense

from .abstract import Device


class FadeType(IntEnum):
    OFF: int = 0
    SLOW: int = 1
    FAST: int = 2


class Touchled(Device):
    """
    Use this class when programming with the touch LED device.
    """
    def __init__ (self, index):
        """"""

    @act
    def default_fade(self, fadeType):
        """
        Sets the default fade time for the touchled sensor.

        Params:
        fadeType: The type of fade the touchled will use: FadeType.SLOW, FAST or OFF
        """

    @sense
    def pressing(self):
        """
        Get the pressed status of the touchled device.

        Returns True if pressed, False otherwise
        """

    @act
    def on(self, color, brightness=100):
        """
        Turn on the led in the touchled sensor.

        Params:
        color: color value: 0xRRGGBB
        brightness: The brightness for the led

        """

    @act
    def on_hue(self, colorHue, brightness=100):
        """
        Turn on the led in the touchled sensor.

        Params:
        colorHue: The color of the led: ColorHue enum value
        brightness: The brightness for the led
        """

    @act
    def on_rgb(self, red, green, blue, brightness=100):
        """
        Turn on the led in the touchled sensor.

        Params:
        red: The red value of the led, 0-255
        green: The green value of the led, 0-255
        blue: The blue value of the led, 0-255
        brightness: The brightness for the led, 0-100
        """

    @act
    def off(self):
        """
        Turn off the led in the touchled sensor.
        """

    @act
    def brightness(self, brightness):
        """
        Turn on the led in the touchled sensor, or change current brightness.

        Params:
        brightness: The brightness for the led 0-100
        """

    @act
    def blink(self, color, on_time=0.25, off_time=0.25):
        """
        Set the led in the touchled sensor as blinking.

        Params:
        color: color value: 0xRRGGBB
        on_time: The time the led should remain on in seconds
        off_time: The time the led should remain off in seconds

        """

    @act
    def blink_hue(self, colorHue, on_time=0.25, off_time=0.25):
        """
        Set the led in the touchled sensor as blinking.

        Params:
        colorHue: The color of the led: ColorHue enum value
        on_time: The time the led should remain on in seconds
        off_time: The time the led should remain off in seconds
        """

    @act
    def blink_rgb(self, red, green, blue, on_time=0.25, off_time=0.25):
        """
        Set the led in the touchled sensor as blinking.

        Params:
        red: The red value of the led 0-255
        green: The green value of the led 0-255
        blue: The blue value of the led 0-255
        on_time: The time the led should remain on in seconds
        off_time: The time the led should remain off in seconds
        """