"""VEX Color Sensor."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from .color_hue import ColorHue


__all__: Sequence[str] = 'Colorsensor', 'ColorHue'


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_colorsensor.html
""")
class ColorSensor(Device):
    """VEX Color Sensor."""

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
        """Check Equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.is_grayscale == self.is_grayscale) and
                (other.proximity == self.proximity))

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.port, self.is_grayscale, self.proximity))

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


# alias
Colorsensor = ColorSensor
