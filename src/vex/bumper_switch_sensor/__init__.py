"""Bumper Switch Sensor."""


from collections.abc import Sequence
from threading import Thread

from abm.decor import sense

from .._abstract_device import Device
from ..brain.port import Ports

from .._util.doc import robotmesh_doc, vexcode_doc


__all__: Sequence[str] = ('Bumper',)


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_bumper.html
""")
class Bumper(Device):
    """Bumper Switch Sensor."""

    @robotmesh_doc("""
        Creates a new bumper object on the port specified in the parameter.

        param:
        index: The port index for this bumper. The index is zero-based.
    """)
    def __init__(self, index: Ports, /):
        """Initialize Bumper Switch Sensor."""
        self.port: Ports = index

    def __hash__(self) -> int:
        """Return integer hash."""
        raise hash(self.port)

    @robotmesh_doc("""
        Get the pressed status of the bumper device.

        Returns True if pressed, False otherwise.
    """)
    @vexcode_doc("""
        Pressing Bumper

        Reports if a VEX IQ Bumper is currently being pressed.

        Pressing Bumper reports True if the Bumper is being pressed.
        Pressing Bumper reports False if the Bumper is not being pressed.
    """)
    @sense
    def pressing(self) -> bool:
        """Return pressed status."""

    @vexcode_doc("""
        Bumper Pressed

        Runs the specified callback function when a bumper is pressed.

        You will need to create a function to call
        when the Bumper Sensor is pressed.
        Provide the name of the function that should run when the event occurs
        as the callback parameter.

        Then, the function is passed as the parameter of the Bumper Pressed
        function call.

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    def pressed(self, callback: callable, /):
        """Trigger callback function upon being pressed."""
        def trigger_callback_whenever_pressing():
            while True:
                if self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()

    @vexcode_doc("""
        Bumper Released

        Runs the specified function when a bumper is released.

        Create a function to call when the Bumper is released.
        Provide the name of the function that should run when the event occurs
        as the callback parameter.

        Then, the function is passed as the parameter of the Bumper Released
        function call.

        A callback function is a function passed into another function
        as an argument. The code inside the callback function will run
        whenever the event occurs.
    """)
    def released(self, callback: callable, /):
        """Trigger callback function upon being released."""
        def trigger_callback_whenever_not_pressing():
            while True:
                if not self.pressing():
                    callback()

        Thread(group=None, target=trigger_callback_whenever_not_pressing, name=None,  # noqa: E501
               args=(), kwargs={}, daemon=True).start()
