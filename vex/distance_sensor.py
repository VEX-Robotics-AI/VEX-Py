from __decor import return_qualname_and_args

from .abstract import Device


@return_qualname_and_args
class Sonar(Device):
    ...
