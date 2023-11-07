"""Joystick axis."""


from collections.abc import Callable, Sequence
from threading import Thread
from typing import LiteralString, Self, TypeVar  # noqa: F401

from abm.decor import sense

from .._util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[LiteralString] = ('ControllerAxis',)


Controller = None  # *** FIXME: TypeVar(name='Controller') causes segfault! ***


@robotmesh_doc("""
    Use the Axis class to get values from one of the controller's joysticks

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller_axis.html
""")
class ControllerAxis:
    """Joystick axis."""

    def __init__(self: Self, parent: Controller, axtype: LiteralString):
        """Initialize Controller Joystick Axis."""
        self.parent: Controller = parent
        self.axtype: LiteralString = axtype

    def __eq__(self: Self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, ControllerAxis) and
                (other.parent == self.parent) and
                (other.axtype == self.axtype))

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        return hash((self.parent, self.axtype))

    def __repr__(self: Self):
        """Return string representation."""
        return f'{type(self).__name__}({self.axtype})'

    @robotmesh_doc("""
        Gets the value of the joystick axis on a scale from -127 to 127.

        Returns an integer that represents the value of the joystick axis.
    """)
    @sense
    def value(self: Self) -> int:
        """Return raw position value."""

    @robotmesh_doc("""
        Gets the position of the joystick axis on a scale from -100 to 100.

        Returns an integer that represents the position of the joystick axis.
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
    def position(self: Self) -> int:
        """Return percentage position."""

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
    def changed(self: Self, callback: Callable, /):
        """Trigger callback function upon being moved."""
        def trigger_callback_whenever_changed():
            while True:
                if self.position() != self.position():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_changed, name=None,
               args=(), kwargs={}, daemon=True).start()
