"""Color Sensor."""


from collections.abc import Sequence
from typing import Literal
from typing_extensions import Self

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..units_common.numeric import PERCENT
from ..util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = 'ColorSensor', 'Colorsensor'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_colorsensor.html
""")
class ColorSensor(Device):
    """Color Sensor."""

    @robotmesh_doc("""
        Create new color sensor object on the port specified in the parameter.

        Parameters:
        - index: The port index (zero-based)
        - is_grayscale: Whether grayscale mode (LED on), default false
        - proximity: threshold (default 700)
    """)
    def __init__(self, index: Ports,
                 is_grayscale: bool = False, proximity: float = 700, /):
        """Initialize Color Sensor."""
        self.port: Ports = index
        self.is_grayscale: bool = is_grayscale
        self.proximity: float = proximity

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.is_grayscale == self.is_grayscale) and
                (other.proximity == self.proximity))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.port, self.is_grayscale, self.proximity))

    @vexcode_doc("""
        Set Color Sensor Light

        Sets the brightness of the VEX IQ Color Sensor's light.

        The Color Sensor has a light source that can be adjusted
        to help detect the color of an object or a surface.

        Set Color Sensor Light accepts
        a range of 0 to 100 for the BRIGHTNESS parameter.

        The higher the value is set, the brighter the Color Sensor's
        light source will shine.
    """)
    @act
    def set_light(self, brightness: int = 50, unit: Literal[PERCENT] = PERCENT):  # noqa: E501
        """Set light's brightness percentage level."""

    @vexcode_doc("""
        Color Is Near Object

        Reports if a VEX IQ Color Sensor detects an object or surface.

        Reports True when a Color Sensor detects an object or surface
        close to the front of the sensor.

        Reports False when a Color Sensor does not detect an object or surface
        close to the front of the sensor.
    """)
    @sense
    def is_near_object(self) -> bool:
        """Detect whether there is an object/surface near sensor's front."""

    @robotmesh_doc("""
        Get the name of the detected color.

        Returns:
        enum value for the closest color detected
        out of ColorHue.RED, GREEN or BLUE (or NONE).
    """)
    @sense
    def colorname3(self) -> int:
        """Return one of RED, GREEN and BLUE."""

    @robotmesh_doc("""
        Get the name of the detected color.

        Returns:
        enum value of the closest color detected out of 12
        possible values of ColorType (or NONE).
    """)
    @sense
    def colorname12(self) -> int:
        """Return one of 12 colors or NONE."""

    @robotmesh_doc("""
        Get the grayscale value detected by the color sensor.

        Parameters:
        - raw: if True, raw value will be returned, otherwise a percentage

        Returns:
        integer that represents the detected grayscale value
        (percentage 0-100 or raw 0-1024).
    """)
    @sense
    def grayscale(self, raw: bool = False, /) -> int:
        """Return grayscale value."""

    @robotmesh_doc("""
        Check to see if an object is detected by the color sensor.

        Returns:
        True if an object has been detected, False otherwise
    """)
    @sense
    def near(self) -> bool:
        """Check if there is a nearly object."""

    @robotmesh_doc("""
        Set the `near` threshold setting.

        Parameters:
        - proximity: threshold (higher is closer) (default 700)
    """)
    @act
    def set_proximity_threshold(self, proximity: float = 700, /):
        """Set threshold for proximity."""
        self.proximity: float = proximity

    @robotmesh_doc("""
        Turn the led on the color sensor on or off.

        Parameters:
        - state: if True, LED will be turned on
    """)
    @act
    def led(self, state: bool, /):
        """Set LED state."""

    @vexcode_doc(
        """
        Color
        Reports the color currently being detected by a VEX IQ Color Sensor.

            color.color()

        How To Use
        Compare the value returned by Color to one of the following colors to check if a specific color is being detected:

            Color.RED
            Color.RED_VIOLET
            Color.VIOLET
            Color.BLUE_VIOLET
            Color.BLUE
            Color.BLUE_GREEN
            Color.GREEN
            Color.YELLOW_GREEN
            Color.YELLOW
            Color.YELLOW_ORANGE
            Color.ORANGE
            Color.RED_ORANGE

        Example
        The example below prints "Red" to the IQ Brain's screen if a red object is currently being detected by a Color Sensor.

        if color.color() == Color.RED:
            brain.screen.print("Red")

        """
    )
    @sense
    def color(self):
        """Return the color currently being detected."""

    @vexcode_doc(
        """
        Color Brightness
        Reports the amount of light detected by a VEX IQ Color Sensor.

            color.brightness()

        How To Use
        Color Brightness reports a range of values from 0 to 100 percent.

        A larger amount of light will report a higher value, while a smaller amount of light will report a lower value.

        Example
        The example below prints the amount of light detected by a Color Sensor.

            brain.screen.print("Brightness:", color.brightness())
        """
    )
    @sense
    def brightness(self):
        """Return the amount of light detected by the Color Sensor."""

    @vexcode_doc(
        """
        Color Hue
        Reports the hue of the color detected by a VEX IQ Color Sensor.

            color.hue()

        How To Use
        Color Hue reports a range of values from 0 to 360 degrees, which represents the position of the color on the color wheel.

        Example
        The example prints the hue of the color detected by the Color Sensor.

            brain.screen.print("Hue:", color.hue())
        """
    )
    @sense
    def hue(self):
        """Return the hue of the color detected by a VEX IQ Color Sensor."""


# alias
Colorsensor = ColorSensor
