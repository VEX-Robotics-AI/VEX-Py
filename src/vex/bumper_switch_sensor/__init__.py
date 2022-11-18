"""VEX Bumper Switch Sensor."""


from collections.abc import Sequence

from abm.decor import sense, act

from .._abstract_device import Device
from ..brain.port import Ports

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401


__all__: Sequence[str] = ('Bumper',)


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

    @vexcode_doc("""
        Bumper Pressed
            Runs the specified callback function when a bumper is pressed.
            bumper.pressed(callback)
    
        How To Use
        You will need to create a function to call when the Bumper Sensor is pressed. Provide the name of the function that should run when the event occurs as the callback parameter.

        def bumper_pressed():
            brain.screen.print("Bumper Pressed")
        
        Then, the function is passed as the parameter of the Bumper Pressed function call.
        bumper.pressed(bumper_pressed)

        Callback Functions
        A callback function is a function passed into another function as an argument. The code inside the callback function will run whenever the event occurs.

        def callback_function():
            brain.screen.print("Pressed")

        bumper.pressed(callback_function)
    """)  
    @act
    def pressed(self, callback):
        """Return the specified callback function when a bumper is pressed"""


    @vexcode_doc("""
    Bumper Released
    Runs the specified function when a bumper is released.
        bumper.released(callback)
    
    How To Use
    Create a function to call when the Bumper is released. Provide the name of the function that should run when the event occurs as the callback parameter.

    def bumper_released():
        brain.screen.print("Bumper released")
    
    Then, the function is passed as the parameter of the Bumper Released function call.
        bumper.released(bumper_released)
    
    Callback Functions
    A callback function is a function passed into another function as an argument. The code inside the callback function will run whenever the event occurs.

    def callback_function():
        brain.screen.print("Released")

    bumper.released(callback_function)
    """)
    @act 
    def released(self, callback):
        """Return the specified callback function when bumper is released"""
