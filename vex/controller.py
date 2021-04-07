from __decor import act, sense

from vex.abstract import DeviceWithoutPort


class Controller(DeviceWithoutPort):
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """


class ControllerAxis(DeviceWithoutPort):
    """
    Use the axis class to get values from one of the controller's joysticks.
    """


class ControllerButton(DeviceWithoutPort):
    """
    Use the button class to get values from the controller's buttons.
    """
