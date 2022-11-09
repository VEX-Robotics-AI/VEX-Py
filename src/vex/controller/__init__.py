"""VEX Controller."""


from __future__ import annotations

from collections.abc import Sequence

from abm.decor import act

from .._abstract_device import SingletonDevice

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from .axis import ControllerAxis
from .button import ControllerButton


__all__: Sequence[str] = 'Controller', 'ControllerButton', 'ControllerAxis'


# TODO:
# - add VEXcode doc
# - add L3 & R3 buttons
@robotmesh_doc("""
    Use the Controller class to get values from the remote controller.

    (as well as write to the controller's screen)

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_controller.html
""")
class Controller(SingletonDevice):
    # pylint: disable=too-many-instance-attributes
    """Controller."""

    def __init__(self):
        """Initialize VEX Controller."""
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
        self._buttonRUp: ControllerButton = ControllerButton(mask='RUp')
        self._buttonRDown: ControllerButton = ControllerButton(mask='RDown')

    @robotmesh_doc("""
        Set the value of the controller axis deadband.

        (minimum absolute threshold at which position is reported as non-zero)
    """)
    @act
    def set_deadband(self, deadband: float, /):
        """Set Controller Axis Deadband Percent Threshold."""
        # pylint: disable=attribute-defined-outside-init
        self.deadband: float = deadband

    @property
    def buttonEUp(self) -> ControllerButton:
        """Return Controller Button E-Up."""
        return self._buttonEUp

    @property
    def buttonEDown(self) -> ControllerButton:
        """Return Controller Button E-Down."""
        return self._buttonEDown

    @property
    def buttonFUp(self) -> ControllerButton:
        """Return Controler Button F-Up."""
        return self._buttonFUp

    @property
    def buttonFDown(self) -> ControllerButton:
        """Return Controller Button F-Down."""
        return self._buttonFDown

    @property
    def buttonLUp(self) -> ControllerButton:
        """Return Controller Button L-Up."""
        return self._buttonLUp

    @property
    def buttonLDown(self) -> ControllerButton:
        """Return Controller Button L-Down."""
        return self._buttonLDown

    @property
    def buttonRUp(self) -> ControllerButton:
        """Return Controller Button R-Up."""
        return self._buttonRUp

    @property
    def buttonRDown(self) -> ControllerButton:
        """Return Controller Button R-Down."""
        return self._buttonRDown

    @property
    def axisA(self) -> ControllerAxis:
        """Return Controller Axis A."""
        return self._axisA

    @property
    def axisB(self) -> ControllerAxis:
        """Return Controller Axis B."""
        return self._axisB

    @property
    def axisC(self) -> ControllerAxis:
        """Return Controller Axis C."""
        return self._axisC

    @property
    def axisD(self) -> ControllerAxis:
        """Return Controller Axis D."""
        return self._axisD
