"""Vision Object."""


from ..util.doc import robotmesh_doc


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
        """Return Object ID."""

    @robotmesh_doc("""
        Return the top left x position of the object.
    """)
    @property
    def originX(self) -> int:
        """Return Object's Top-Left X Co-ordinate."""

    @robotmesh_doc("""
        Return the top left y position of the object.
    """)
    @property
    def originY(self) -> int:
        """Return Object's Top-Left Y Co-ordinate."""

    @robotmesh_doc("""
        Return the center x position of the object.
    """)
    @property
    def centerX(self) -> int:
        """Return Object's Center X Co-ordinate."""

    @robotmesh_doc("""
        Return the center y position of the object.
    """)
    @property
    def centerY(self) -> int:
        """Return Object's Center Y Co-ordinate."""

    @robotmesh_doc("""
        Return the width of the object.
    """)
    @property
    def width(self) -> int:
        """Return Object's Width."""

    @robotmesh_doc("""
        Return the height of the object.
    """)
    @property
    def height(self) -> int:
        """Return Object's Height."""

    @robotmesh_doc("""
        Return the angle of the object.
    """)
    @property
    def angle(self) -> int:
        """Return Object's Angle."""

    @robotmesh_doc("""
        Return True if vision sensor detects the object, False if not.
    """)
    @property
    def exists(self) -> bool:
        """Check if Object is detected."""
