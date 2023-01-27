"""Vision object."""


from collections.abc import Sequence
from typing import LiteralString, Self

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('VisionObject',)


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvision_1_1_vision_object.html
""")
class VisionObject:
    """Vision object."""

    @robotmesh_doc("""
        Unique ID of the object.
    """)
    @property
    def id(self: Self) -> int:
        """Return object ID."""

    @robotmesh_doc("""
        Top-left X position of the object.
    """)
    @property
    def originX(self: Self) -> int:
        """Return object's top-left X co-ordinate."""

    @robotmesh_doc("""
        Top-left Y position of the object.
    """)
    @property
    def originY(self: Self) -> int:
        """Return object's top-left Y co-ordinate."""

    @robotmesh_doc("""
        Center X position of the object.
    """)
    @property
    def centerX(self: Self) -> int:
        """Return object's center X co-ordinate."""

    @robotmesh_doc("""
        Center Y position of the object.
    """)
    @property
    def centerY(self: Self) -> int:
        """Return object's center Y co-ordinate."""

    @robotmesh_doc("""
        Width of the object.
    """)
    @property
    def width(self: Self) -> int:
        """Return object's width."""

    @robotmesh_doc("""
        Height of the object.
    """)
    @property
    def height(self: Self) -> int:
        """Return object's height."""

    @robotmesh_doc("""
        Angle of the object.
    """)
    @property
    def angle(self: Self) -> int:
        """Return object's angle."""

    @robotmesh_doc("""
        True if vision sensor detects the object, False if not.
    """)
    @property
    def exists(self: Self) -> bool:
        """Check if object is detected."""
