"""Temperature units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc


__all__: Sequence[LiteralString] = ('TemperatureUnits',)


@robotmesh_doc("""
    Measurement units for temperature values

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_temperature_units.html
""")
class TemperatureUnits(IntEnum):
    """Temperature units."""

    CELCIUS: int = 0
    FAHRENHEIT: int = 1
    PCT: int = 0xFF
