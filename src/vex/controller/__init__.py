"""Controller."""


from collections.abc import Sequence
from typing import LiteralString, Optional, Self

from abm.decor import act

from .._abstract_device import SingletonDevice

from .._util.doc import robotmesh_doc

from .axis import ControllerAxis
from .button import ControllerButton
from .type import ControllerType, PRIMARY, PARTNER


__all__: Sequence[LiteralString] = ('Controller',
                                    'ControllerAxis',
                                    'ControllerButton',
                                    'ControllerType', 'PRIMARY', 'PARTNER')


@robotmesh_doc("""
    Use the Controller class to get values from the remote controller
    as well as write to the controller's screen

    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller.html
""")
class Controller(SingletonDevice):
    # pylint: disable=too-many-instance-attributes
    """Controller."""

    def __init__(self: Self):
        """Initialize Controller."""
        self._axisA: ControllerAxis = ControllerAxis(parent=self, axtype='A')
        self._axisB: ControllerAxis = ControllerAxis(parent=self, axtype='B')
        self._axisC: ControllerAxis = ControllerAxis(parent=self, axtype='C')
        self._axisD: ControllerAxis = ControllerAxis(parent=self, axtype='D')
        self._buttonEUp: ControllerButton = ControllerButton(mask='EUp')
        self._buttonEDown: ControllerButton = ControllerButton(mask='EDown')
        self._buttonFUp: ControllerButton = ControllerButton(mask='FUp')
        self._buttonFDown: ControllerButton = ControllerButton(mask='FDown')
        self._buttonLUp: ControllerButton = ControllerButton(mask='LUp')
        self._buttonLDown: ControllerButton = ControllerButton(mask='LDown')
        self._buttonL3: ControllerButton = ControllerButton(mask='L3')
        self._buttonRUp: ControllerButton = ControllerButton(mask='RUp')
        self._buttonRDown: ControllerButton = ControllerButton(mask='RDown')
        self._buttonR3: ControllerButton = ControllerButton(mask='R3')

        self.deadband: Optional[int] = None

    @robotmesh_doc("""
        Set the value of the controller axis deadband
        (minimum absolute threshold at which position is reported as non-zero)
    """)
    @act
    def set_deadband(self: Self, deadband: int, /):
        """Set joystick axis deadband percentage threshold."""
        self.deadband: int = deadband

    @property
    def buttonEUp(self: Self) -> ControllerButton:
        """Get button E Up."""
        return self._buttonEUp

    @property
    def buttonEDown(self: Self) -> ControllerButton:
        """Get button E Down."""
        return self._buttonEDown

    @property
    def buttonFUp(self: Self) -> ControllerButton:
        """Get button F Up."""
        return self._buttonFUp

    @property
    def buttonFDown(self: Self) -> ControllerButton:
        """Get button F Down."""
        return self._buttonFDown

    @property
    def buttonLUp(self: Self) -> ControllerButton:
        """Get button L Up."""
        return self._buttonLUp

    @property
    def buttonL3(self: Self) -> ControllerButton:
        """Get button L 3."""
        return self._buttonL3

    @property
    def buttonLDown(self: Self) -> ControllerButton:
        """Get button L Down."""
        return self._buttonLDown

    @property
    def buttonRUp(self: Self) -> ControllerButton:
        """Get button R Up."""
        return self._buttonRUp

    @property
    def buttonRDown(self: Self) -> ControllerButton:
        """Get button R Down."""
        return self._buttonRDown

    @property
    def buttonR3(self: Self) -> ControllerButton:
        """Get button R 3."""
        return self._buttonR3

    @property
    def axisA(self: Self) -> ControllerAxis:
        """Get axis A."""
        return self._axisA

    @property
    def axisB(self: Self) -> ControllerAxis:
        """Get axis B."""
        return self._axisB

    @property
    def axisC(self: Self) -> ControllerAxis:
        """Get axis C."""
        return self._axisC

    @property
    def axisD(self: Self) -> ControllerAxis:
        """Get axis D."""
        return self._axisD
