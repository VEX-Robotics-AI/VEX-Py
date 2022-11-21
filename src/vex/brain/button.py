"""Brain Buttons."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import sense

from .._util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = ('BrainButton',)


@robotmesh_doc("""
    Use the Button class to get values from the Brain's buttons.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_brain_button.html
""")
class BrainButton:
    """Brain Button."""

    def __init__(self, id: str):   # pylint: disable=redefined-builtin
        """Initialize Brain Button."""
        self.id: str = id

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return isinstance(other, BrainButton) and (other.id == self.id)

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash(self.id)

    def __repr__(self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.id})'

    @robotmesh_doc("""
        Get the pressed status of a button.

        Returns: True if pressed, False otherwise.
    """)
    @vexcode_doc("""
        Reports if the specified button on the VEX IQ Brain is being pressed.

        Reports True if the specified Brain button is pressed.
        Reports False if the specified Brain button is not pressed.

        After `brain.` enter a Brain button to receive the pressed status on.

        Supported Brain buttons are as follows:
        - buttonUp / buttonLeft
        - buttonDown / buttonRight
        - buttonCheck
    """)
    @sense
    def pressing(self) -> bool:
        """Return Button's pressed status."""
