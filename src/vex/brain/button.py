"""Brain Buttons."""


from typing_extensions import Self

from abm.decor import sense


class BrainButton:
    """Use the button class to get values from the brain's buttons."""

    def __init__(self, id: str):   # pylint: disable=redefined-builtin
        """Initialize BrainButton."""
        self.id: str = id

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, BrainButton) and (other.id == self.id)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash(self.id)

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.id})'

    @sense
    def pressing(self) -> bool:
        """
        Get the pressed status of a button.

        Returns
        True if pressed, False otherwise.
        """
