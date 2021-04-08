from __decor import act, sense

from vex.abstract import SingletonDevice


class Controller(SingletonDevice):
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """
    def __init__(self):
        # !FIXME: mask="EUp", axtype="A" are assumptions
        self._buttonEUp: ControllerButton = ControllerButton(mask="EUp")
        self._buttonEDown: ControllerButton = ControllerButton(mask="EDown")
        self._buttonFUp: ControllerButton = ControllerButton(mask="FUp")
        self._buttonFDown: ControllerButton = ControllerButton(mask="FDown")
        self._buttonLUp: ControllerButton = ControllerButton(mask="LUp")
        self._buttonLDown: ControllerButton = ControllerButton(mask="LDown")
        self._buttonRUp: ControllerButton = ControllerButton(mask="RUp")
        self._buttonRDown: ControllerButton = ControllerButton(mask="RDown")
        self._axisA: ControllerAxis = ControllerAxis(axtype="A")
        self._axisB: ControllerAxis = ControllerAxis(axtype="B")
        self._axisC: ControllerAxis = ControllerAxis(axtype="C")
        self._axisD: ControllerAxis = ControllerAxis(axtype="D")

    @act
    def set_deadband(self, deadband):
        """
        set the value of the controller axis deadband (minimum absolute threshold at which position is reported as non-zero) move to c-variable for deadband
        """
        pass

    @property
    def buttonEUp(self) -> ControllerButton:
        return self._buttonEUp

    @property
    def buttonEDown(self) -> ControllerButton:
        return self._buttonEDown

    @property
    def buttonFUp(self) -> ControllerButton:
        return self._buttonFUp

    @property
    def buttonFDown(self) -> ControllerButton:
        return self._buttonFDown

    @property
    def buttonLUp(self) -> ControllerButton:
        return self._buttonLUp

    @property
    def buttonLDown(self) -> ControllerButton:
        return self._buttonLDown

    @property
    def buttonRUp(self) -> ControllerButton:
        return self._buttonRUp

    @property
    def buttonRDown(self) -> ControllerButton:
        return self._buttonRDown

    @property
    def axisA(self) -> ControllerAxis:
        return self._axisA

    @property
    def axisB(self) -> ControllerAxis:
        return self._axisB

    @property
    def axisC(self) -> ControllerAxis:
        return self._axisC

    @property
    def axisD(self) -> ControllerAxis:
        return self._axisD


class ControllerAxis:
    """
    Use the axis class to get values from one of the controller's joysticks.
    """
    def __init__ (self, parent, axtype):
        """"""
        pass

    @sense
    def value(self) -> int:
        """
        Gets the value of the joystick axis on a scale from -127 to 127.

        Returns
        an integer that represents the value of the joystick axis.
        """
        pass

    @sense
    def position(self) -> int:
        """
        Gets the position of the joystick axis on a scale from -100 to 100.

        Returns
        an integer that represents the position of the joystick axis.
        """
        pass


class ControllerButton:
    """
    Use the button class to get values from the controller's buttons.
    """
    def __init__(self, mask):
        self.mask = mask

    def __str__(self) -> str:
        return f'{type(self).__name__}({self.id})'

    @sense
    def pressing(self) -> bool:
        """
        Gets the status of a button

        Returns:
        True if pressed, false otherwise
        """
        pass