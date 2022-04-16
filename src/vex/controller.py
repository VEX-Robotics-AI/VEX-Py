"""VEX Controller."""


from __future__ import annotations

from collections.abc import Sequence

from __vex.decor import act, sense

from vex.abstract import SingletonDevice


__all__: Sequence[str] = 'Controller', 'ControllerButton', 'ControllerAxis'


class Controller(SingletonDevice):
    # pylint: disable=too-many-instance-attributes
    """
    Use the controller class to get values from the remote controller.

    (as well as write to the controller's screen)
    """

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

    @act
    def set_deadband(self, deadband: float):
        """
        Set the value of the controller axis deadband.

        (minimum absolute threshold at which position is reported as non-zero)
        """
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


class ControllerAxis:
    """Use the axis class to get values from one of the controller's joysticks."""   # noqa: E501

    def __init__(self, parent: Controller, axtype: str):
        """Initialize Controller Axis."""
        self.parent: Controller = parent
        self.axtype: str = axtype

    def __repr__(self):
        """Return string representation."""
        return f'{type(self).__name__}({self.axtype})'

    @sense
    def value(self) -> int:
        """
        Get the value of the joystick axis on a scale from -127 to 127.

        Returns
        an integer that represents the value of the joystick axis.
        """

    @sense
    def position(self) -> int:
        """
        Get the position of the joystick axis on a scale from -100 to 100.

        Returns
        an integer that represents the position of the joystick axis.
        """


class ControllerButton:
    """Use the button class to get values from the controller's buttons."""

    def __init__(self, mask: str):
        """Initialize Controller Button."""
        self.mask: str = mask

    def __repr__(self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.mask})'

    @sense
    def pressing(self) -> bool:
        """
        Get the status of a button.

        Returns:
        True if pressed, false otherwise
        """
