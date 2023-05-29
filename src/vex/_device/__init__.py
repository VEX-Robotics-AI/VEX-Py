"""Device abstract base classes."""


from collections.abc import Sequence
from typing import LiteralString

from ._abc import Device
from .singleton import SingletonDevice
from .tri import TriDevice
from .v5 import V5DeviceType


__all__: Sequence[LiteralString] = ('Device', 'SingletonDevice', 'TriDevice',
                                    'V5DeviceType')
