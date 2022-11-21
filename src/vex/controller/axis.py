"""Controller Axes (A, B, C, D)."""


from collections.abc import Sequence
from typing import TypeVar
from typing_extensions import Self

from abm.decor import act, sense

from .._util.doc import robotmesh_doc, vexcode_doc


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
        """Check equality."""
        return isinstance(other, ControllerAxis) and \
            (other.parent == self.parent) and (other.axtype == self.axtype)

    def __hash__(self) -> int:
        """Return integer hash."""
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
    @vexcode_doc("""
        Controller Axis Position

        Reports the position of a joystick on the VEX IQ Controller
        along the specified axis.

        Controller Axis Position reports a range between -100 to 100.

        Controller Axis Position will report 0 when joystick axis is centered.

        Choose which Controller axis to report.
        - axisA: left joystick (up and down)
        - axisB: left joystick (left and right)
        - axisC: right joystick (left and right)
        - axisD: right joystick (up and down)
    """)
    @sense
    def position(self) -> int:
        """Return controller joystick axis percent position."""

    @vexcode_doc("""
        Controller Axis Changed

        Runs the provided callback funtion
        when the selected VEX IQ Controller's joystick axis is moved.

        You will need to create a callback function to call
        when a joystick axis on the Controller is moved.

        Choose which Controller joystick axis
        to use and pass the callback function:
        - axisA
        - axisB
        - axisC
        - axisD

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    @act
    def changed(self, callback: callable, /):
        """Trigger callback function when controller axis is changed."""
        callback()
