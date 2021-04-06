from .abstract import Device, Enum


class BrakeType(Enum):
    """
    The defined units for brake values.
    """
    COAST: int = 0   # A brake unit that is defined as coast.
    BRAKE: int = 1   # A brake unit that is defined as brake.
    HOLD: int = 2   # A brake unit that is defined as hold.


class DirectionType(Enum):
    """
    The defined units for direction values.
    """
    FWD: int = 0   # A direction unit that is defined as forward.
    REV: int = 1   # A direction unit that is defined as backward.


class Motor(Device):
    ...
