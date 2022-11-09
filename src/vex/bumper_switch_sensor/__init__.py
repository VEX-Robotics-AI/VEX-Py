"""VEX Bumper Switch Sensor."""


from collections.abc import Sequence

from abm.decor import sense

from .._abstract_device import Device
from ..brain.port import Ports

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('Bumper',)


# TODO: add VEXcode doc
@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_bumper.html
""")
class Bumper(Device):
    """Bumper Switch Sensor."""

    @robotmesh_doc("""
        Create a new bumper object on the port specified in the parameter.

        param:
        index: The port index for this bumper. The index is zero-based.
    """)
    def __init__(self, index: Ports, /):
        """Initialize Bumper Switch Sensor."""
        self.port: Ports = index

    def __hash__(self) -> int:
        """Return Integer Hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Get the pressed status of the bumper device.

        Returns
        True if pressed, False otherwise.
    """)
    @sense
    def pressing(self) -> bool:
        """Return Bumper's pressed status."""
