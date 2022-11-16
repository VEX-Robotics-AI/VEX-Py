"""Controller Buttons."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import sense, act

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from typing import Callable

__all__: Sequence[str] = ('ControllerButton',)


@robotmesh_doc("""
    Use the Button class to get values from the controller's buttons.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller_button.html
""")
class ControllerButton:
    """Controller Button."""

    def __init__(self, mask: str):
        """Initialize Controller Button."""
        self.mask: str = mask

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, ControllerButton) and (other.mask == self.mask)   # noqa: E501

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash(self.mask)

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.mask})'

    @robotmesh_doc("""
        Get the status of a button.

        Returns:
        True if pressed, false otherwise
    """)
    @sense
    def pressing(self) -> bool:
        """Return Controller Button's pressed status."""
    @vexcode_doc("""
        Controller Button Pressed
        Runs the callback function when the VEX IQ Controller button is pressed.

            controller.button.pressed(callback)

        How To Use
        You will need to create a callback function that will be called when a Controller button is pressed.

        Choose which Controller button to call the Controller Button Pressed function with:

            buttonEUp
            buttonEDown
            buttonFUp
            buttonFDown
            buttonLUp
            buttonLDown
            buttonRUp
            buttonRDown
            buttonL3
            buttonR3
            Example
        The example below prints to the IQ Brain's screen when the Controller's L3 button is pressed.

            def button_pressed():
                brain.screen.print("Button pressed")
                
            controller.buttonL3.pressed(button_pressed)""")
    @act
    def pressed(self, callback):
        """Runs the callback function when the VEX IQ Controller button is pressed."""


