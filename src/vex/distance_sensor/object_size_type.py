
"""Object Size Type."""


from collections.abc import Sequence
from enum import IntEnum, auto

from ..util.doc import vexcode_doc


__all__: Sequence[str] = ("ObjectSizeType",)


@vexcode_doc(
    """VEX IQ (2nd generation) Object Size Type."""
)
class ObjectSizeType(IntEnum):
    """VEX IQ (2nd generation) Object Size Type."""

    SMALL: int = auto()
    MEDIUM: int = auto()
    LARGE: int = auto()
