"""Controller Axes (A, B, C, D)."""


from collections.abc import Sequence
from typing import TypeVar
from typing_extensions import Self

from abm.decor import sense

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('ControllerAxis',)


Controller = TypeVar(name='Controller')


@robotmesh_doc("""
    Use the Axis class to get values from one of the controller's joysticks.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller_axis.html
""")
class ControllerAxis:
    """Controller Joystick Axis."""

    def __init__(self, parent: Controller, axtype: str):
        """Initialize Controller Axis."""
        self.parent: Controller = parent
        self.axtype: str = axtype

    def __eq__(self, other: Self) -> bool:
        """Check Equality."""
        return isinstance(other, ControllerAxis) and \
            (other.parent == self.parent) and (other.axtype == self.axtype)

    def __hash__(self) -> int:
        """Return Integer Hash."""
        return hash((self.parent, self.axtype))

    def __repr__(self):
        """Return String Representation."""
        return f'{type(self).__name__}({self.axtype})'

    @robotmesh_doc("""
        Get the value of the joystick axis on a scale from -127 to 127.

        Returns
        an integer that represents the value of the joystick axis.
    """)
    @sense
    def value(self) -> int:
        """Return Controller Joystick Axis Raw Value."""

    @robotmesh_doc("""
        Get the position of the joystick axis on a scale from -100 to 100.

        Returns
        an integer that represents the position of the joystick axis.
    """)
    @sense
    def position(self) -> int:
        """Return Controller Joystick Axis Percent Position."""
