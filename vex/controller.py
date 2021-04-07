from __decor import return_qualname_and_args

from vex.abstract import DeviceWithoutPort


@return_qualname_and_args
class Controller(DeviceWithoutPort):
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """


@return_qualname_and_args
class ControllerAxis(DeviceWithoutPort):
    """
    Use the axis class to get values from one of the controller's joysticks.
    """


@return_qualname_and_args
class ControllerButton(DeviceWithoutPort):
    """
    Use the button class to get values from the controller's buttons.
    """
