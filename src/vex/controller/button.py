"""Controller Buttons."""


from collections.abc import Sequence
from typing_extensions import Self

from abm.decor import sense


__all__: Sequence[str] = ('ControllerButton',)


class ControllerButton:
    """Use the button class to get values from the controller's buttons."""

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

    @sense
    def pressing(self) -> bool:
        """
        Get the status of a button.

        Returns:
        True if pressed, false otherwise
        """
