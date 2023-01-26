"""Optical Sensor."""


from collections.abc import Sequence
from threading import Thread
from typing import Literal

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from .._common_enums.color import Color
from .._common_enums.percent import PERCENT

from .._util.doc import vexcode_doc

from .gesture_info import GestureInfo
from .gesture_type import GestureType
from .led_state import LedStateType


__all__: Sequence[str] = 'Optical', 'GestureType', 'LedStateType'


GESTURE_CALLBACK_DOCSTR: str = """
    Optical Gesture Detected

    Runs the callback function
    when gesture is detected by an IQ Optical Sensor.

    The Optical Gesture Detected command can be used to trigger
    actions or behaviors when a gesture is detected by an IQ Optical Sensor.

    You will need to create a function to call when a gesture is detected.
    Provide the name of the function that should run when the event occurs
    as the callback parameter.

    You will also need to ensure that the Optical Sensor is set
    to detect gestures by calling optical.gesture_enable()
    before gesture commands are used.

    Optical Gesture Detected can be used to detect four different gestures:
        gesture_up
        gesture_down
        gesture_left
        gesture_right
"""


class Optical(Device):
    """Optical Sensor."""

    def __init__(self, port: Ports, /):
        """Initialize Optical Sensor."""
        self.port: Ports = port

    def __hash__(self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @vexcode_doc("""
        Optical Gesture Disable

        Sets an IQ Optical Sensor to detect colors.

        The Optical Gesture Disable command allows you
        to set an IQ Optical Sensor to detect colors.

        By default, an IQ Optical Sensor will be set to detect colors.
    """)
    @act
    def gesture_disable(self):
        """Disable gesture detection."""

    @vexcode_doc("""
        Set Optical Light

        Sets the light on a VEX IQ Optical Sensor to on or off.

        Set Optical Light allows you to turn the Optical Sensor's light
        on or off. The light lets the sensor see objects if it is looking
        at an object in a dark area.

        To turn the light on you pass LedStateType.ON as the STATE parameter.
        To turn the light off you pass LedStateType.OFF as the STATE parameter.
    """)
    @act
    def set_light(self, state: LedStateType = LedStateType.ON, /):
        """Set light ON/OFF."""

    @vexcode_doc("""
        Sets the light power of a VEX IQ Optical Sensor.

        Set Optical Light Power will change the brightness of the light
        on an Optical Sensor.

        The command accepts a range of 0 to 100 percent for the POWER
        parameter, and PERCENT as the unit.

        If the light is off, this command will turn the light on.
    """)
    @act
    def set_light_power(self, power: int = 50, unit: Literal[PERCENT] = PERCENT, /):  # noqa: E501
        # pylint: disable=unused-argument
        """Set light power percentage level."""
        assert unit is PERCENT, ValueError('*** UNIT MUST BE PERCENT ***')

    @vexcode_doc("""
        Optical Is Near Object

        Reports if a VEX IQ Optical Sensor detects an object in its range.

        Optical Is Near Object returns True if an object is detected,
        and returns False otherwise.

        It should be used to check if an object is close
        to the IQ Optical Sensor so that the color readings
        from the Optical Sensor's color() command are accurate.
    """)
    @sense
    def is_near_object(self) -> bool:
        """Check if Optical Sensor is near an object."""

    @vexcode_doc("""
        Optical Color

        Returns the color detected by a VEX IQ Optical Sensor.

        The Optical Color command returns the closest color match
        based on the hue of a detected object.

        The following colors can be used
        as a comparison to the color detected by an IQ Optical Sensor:
            Color.RED
            Color.GREEN
            Color.BLUE
            Color.YELLOW
            Color.ORANGE
            Color.PURPLE
            Color.CYAN
    """)
    @sense
    def color(self) -> Color:
        """Return closest-matching color hue of detected object."""

    @vexcode_doc("""
        Optical Brightness

        Reports the amount of light detected by a VEX IQ Optical Sensor.

        Optical Brightness reports a range of values from 0 to 100 percent.

        A large amount of light detected will report a high brightness value.
        A small amount of light detected will report a low brightness value.
    """)
    @sense
    def brightness(self) -> int:
        """Return brightness percentage level."""

    @vexcode_doc("""
        Optical Hue

        Reports the hue of the object detected by a VEX IQ Optical Sensor.

        Optical Hue reports a range of values from 0 to 359,
        which represents the location of the detected color on a color wheel.
    """)
    @sense
    def hue(self) -> int:
        """Return color hue value between 0 and 359."""

    @vexcode_doc("""
        Optical Gesture Enable

        Sets an IQ Optical Sensor to detect gestures.

        The Optical Gesture Enable command allows you
        to set an IQ Optical Sensor to detect gestures.

        By default, an IQ Optical Sensor will be set to detect colors.

        Before using any IQ Optical Sensor gesture commands,
        an IQ Optical Sensor must be correctly set to detect gestures.
    """)
    @act
    def gesture_enable(self):
        """Enable gesture detection."""

    @vexcode_doc("""
        Optical Gesture Detected

        Reports detected gesture data from an IQ Optical Sensor.

        The Optical Gesture Detected command returns an object
        with gesture information. To check the type of the detected gesture,
        access the type property on the returned object.

        Before using any IQ Optical Sensor gesture commands,
        an IQ Optical Sensor must be correctly set to detect gestures
        with the optical.gesture_enable() command.

        Below are the gestures that an IQ Optical Sensor can detect:
            GestureType.UP
            GestureType.DOWN
            GestureType.LEFT
            GestureType.RIGHT
    """)
    @sense
    def get_gesture(self) -> GestureInfo:
        """Return an object with gesture information."""

    @vexcode_doc("""
        Optical Object Detected

        Runs the callback function
        when an object is detected by an Optical Sensor.

        The Optical Object Detected command can be used to trigger
        actions or behaviors when an object is detected by an Optical Sensor.

        You will need to create a function to call when an object is detected.
        Provide the name of the function that should run when the event occurs
        as the callback parameter.
    """)
    @act
    def object_detected(self, callback: callable, /):
        """Trigger callback function upon detecting an object."""
        def trigger_callback_whenever_near_object():
            while True:
                if self.is_near_object():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_near_object, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()

    @vexcode_doc("""
        Optical Object Lost

        Runs the callback function when
        a detected object is no longer being detected by an Optical Sensor.

        The Optical Object Lost command can be used to trigger
        actions or behaviors when an Optical Sensor no longer detects
        a previously-detected object.

        You will need to create a function to call when the object is no longer
        being detected. Provide the name of the function that should run
        when the event occurs as the callback parameter.
    """)
    @act
    def object_lost(self, callback: callable, /):
        """Trigger callback function upon losing previously-detected object."""
        def trigger_callback_whenever_not_near_object():
            while True:
                if not self.is_near_object():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_not_near_object,
               name=None, args=(), kwargs={}, daemon=True).start()

    @vexcode_doc(GESTURE_CALLBACK_DOCSTR)
    @act
    def gesture_up(self, callback: callable, /):
        """Trigger callback function upon detecting UP gesture."""
        def trigger_callback_whenever_detecting_up_gesture():
            while True:
                if self.get_gesture().type == GestureType.UP:
                    callback()

        Thread(group=None, target=trigger_callback_whenever_detecting_up_gesture,  # noqa: E501
               name=None, args=(), kwargs={}, daemon=True).start()

    @vexcode_doc(GESTURE_CALLBACK_DOCSTR)
    @act
    def gesture_down(self, callback: callable, /):
        """Trigger callback function upon detecting DOWN gesture."""
        def trigger_callback_whenever_detecting_down_gesture():
            while True:
                if self.get_gesture().type == GestureType.DOWN:
                    callback()

        Thread(group=None, target=trigger_callback_whenever_detecting_down_gesture,  # noqa: E501
               name=None, args=(), kwargs={}, daemon=True).start()

    @vexcode_doc(GESTURE_CALLBACK_DOCSTR)
    @act
    def gesture_left(self, callback: callable, /):
        """Trigger callback function upon detecting LEFT gesture."""
        def trigger_callback_whenever_detecting_left_gesture():
            while True:
                if self.get_gesture().type == GestureType.LEFT:
                    callback()

        Thread(group=None, target=trigger_callback_whenever_detecting_left_gesture,  # noqa: E501
               name=None, args=(), kwargs={}, daemon=True).start()

    @vexcode_doc(GESTURE_CALLBACK_DOCSTR)
    @act
    def gesture_right(self, callback: callable, /):
        """Trigger callback function upon detecting RIGHT gesture."""
        def trigger_callback_whenever_detecting_right_gesture():
            while True:
                if self.get_gesture().type == GestureType.RIGHT:
                    callback()

        Thread(group=None, target=trigger_callback_whenever_detecting_right_gesture,  # noqa: E501
               name=None, args=(), kwargs={}, daemon=True).start()
