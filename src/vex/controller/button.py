"""Controller Buttons."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import sense

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


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
    @sense
    def pressing(self) -> bool:
        """Return Controller Button's pressed status."""
