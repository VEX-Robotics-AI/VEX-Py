"""Controller Buttons."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import sense, act

from .._util.doc import robotmesh_doc, vexcode_doc


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
        """Check equality."""
        return isinstance(other, ControllerButton) and (other.mask == self.mask)   # noqa: E501

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash(self.mask)

    def __repr__(self) -> str:
        """Return String Representation."""
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
    def pressing(self) -> bool:
        """Return Controller Button's pressed status."""

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
    def pressed(self, callback: callable, /):
        """Trigger callback function when controller button is pressed."""
        callback()

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
    def released(self, callback: callable, /):
        """Trigger callback function when controller button is released."""
        callback()
