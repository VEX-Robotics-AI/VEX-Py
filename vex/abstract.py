from abc import abstractproperty
from enum import IntEnum


class Device:
    """
    Base class for all Vex IQ devices.
    """
    @abstractproperty
    def port(self):
        raise NotImplementedError

    def __str__(self):
        return f'{type(self).__name__}@{self.port}'


class Enum(IntEnum):
    ...
