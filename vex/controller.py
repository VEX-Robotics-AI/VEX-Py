from __decor import return_qualname_and_args


@return_qualname_and_args
class Controller:
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """
    def __str__(self) -> str:
        return type(self).__name__


@return_qualname_and_args
class ControllerAxis:
    """
    Use the axis class to get values from one of the controller's joysticks.
    """


@return_qualname_and_args
class ControllerButton:
    """
    Use the button class to get values from the controller's buttons.
    """
