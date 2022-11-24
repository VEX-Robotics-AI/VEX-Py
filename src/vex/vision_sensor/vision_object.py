"""Vision Object."""


from .._util.doc import robotmesh_doc


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvision_1_1_vision_object.html
""")
class VisionObject:
    """Vision Object."""

    @robotmesh_doc("""
        Return the unique ID of the object.
    """)
    @property
    def id(self) -> int:
        """Return object ID."""

    @robotmesh_doc("""
        Return the top left x position of the object.
    """)
    @property
    def originX(self) -> int:
        """Return object's top-left X co-ordinate."""

    @robotmesh_doc("""
        Return the top left y position of the object.
    """)
    @property
    def originY(self) -> int:
        """Return object's top-left Y co-ordinate."""

    @robotmesh_doc("""
        Return the center x position of the object.
    """)
    @property
    def centerX(self) -> int:
        """Return object's center X co-ordinate."""

    @robotmesh_doc("""
        Return the center y position of the object.
    """)
    @property
    def centerY(self) -> int:
        """Return object's center Y co-ordinate."""

    @robotmesh_doc("""
        Return the width of the object.
    """)
    @property
    def width(self) -> int:
        """Return object's width."""

    @robotmesh_doc("""
        Return the height of the object.
    """)
    @property
    def height(self) -> int:
        """Return object's height."""

    @robotmesh_doc("""
        Return the angle of the object.
    """)
    @property
    def angle(self) -> int:
        """Return object's angle."""

    @robotmesh_doc("""
        Return True if vision sensor detects the object, False if not.
    """)
    @property
    def exists(self) -> bool:
        """Check if object is detected."""
