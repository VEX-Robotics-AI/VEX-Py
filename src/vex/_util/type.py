"""Data Types."""


from collections.abc import Sequence
from typing import LiteralString


__all__: Sequence[LiteralString] = ('NumType',)


NumType: type = float | int
