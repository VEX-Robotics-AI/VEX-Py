"""Controller Buttons."""


from collections.abc import Callable, Sequence
from threading import Thread
from typing import LiteralString, Self

from abm.decor import sense, act

from .._util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[LiteralString] = ('ControllerButton',)


@robotmesh_doc("""
    Use the Button class to get values from the controller's buttons

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller_button.html
""")
class ControllerButton:
    """Controller Button."""

    def __init__(self: Self, mask: LiteralString):
        """Initialize Controller Button."""
        self.mask: LiteralString = mask

    def __eq__(self: Self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, ControllerButton) and (other.mask == self.mask)   # noqa: E501

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        return hash(self.mask)

    def __repr__(self: Self) -> LiteralString:
        """Return string representation."""
        return f'{type(self).__name__}({self.mask})'

    @robotmesh_doc("""
        Get the status of a button.

        Returns:
        True if pressed, false otherwise
    """)
    @vexcode_doc("""
        Controller Button Pressing

        Reports if the specified button on the VEX IQ's Controller is pressed.

        Choose which Controller button to detect a press on:
        - buttonEUp
        - buttonEDown
        - buttonFUp
        - buttonFDown
        - buttonLUp
        - buttonLDown
        - buttonRUp
        - buttonRDown
        - buttonL3
        - buttonR3

        Controller Button Pressing reports True
        if the specified Controller button is being pressed.

        Controller Button Pressing reports False
        if the specified Controller button is not being pressed.
    """)
    @sense
    def pressing(self: Self) -> bool:
        """Return pressed status."""

    @vexcode_doc("""
        Controller Button Pressed

        Runs callback function when VEX IQ Controller button is pressed.

        You will need to create a callback function that will be called
        when a Controller button is pressed.

        Choose which Controller button to call the Controller Button Pressed
        function with:
        - buttonEUp
        - buttonEDown
        - buttonFUp
        - buttonFDown
        - buttonLUp
        - buttonLDown
        - buttonRUp
        - buttonRDown
        - buttonL3
        - buttonR3
    """)
    @act
    def pressed(self: Self, callback: Callable, /):
        """Trigger callback function when upon being pressed."""
        def trigger_callback_whenever_pressing():
            while True:
                if self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()

    @vexcode_doc("""
        Controller Button Released

        Runs callback function when VEX IQ Controller button is released.

        You will need to create a callback function that will be called
        when a Controller button is released.

        Choose which Controller button to call the Controller Button Released
        function with:
        - buttonEUp
        - buttonEDown
        - buttonFUp
        - buttonFDown
        - buttonLUp
        - buttonLDown
        - buttonRUp
        - buttonRDown
        - buttonL3
        - buttonR3
    """)
    @act
    def released(self: Self, callback: Callable, /):
        """Trigger callback function upon being released."""
        def trigger_callback_whenever_not_pressing():
            while True:
                if not self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_not_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()
