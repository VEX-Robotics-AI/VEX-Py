from abc import abstractmethod
from enum import IntEnum


class Device:
    """
    Base class for all Vex IQ devices.
    """
    @property
    @abstractmethod
    def port(self):
        raise NotImplementedError

    def __str__(self) -> str:
        return f'{type(self).__name__}@{self.port}'


class DeviceWithoutPort:
    def __str__(self) -> str:
        return type(self).__name__


class Enum(IntEnum):
    ...
