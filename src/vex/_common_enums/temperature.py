"""Temperature units."""


from collections.abc import Sequence
from enum import IntEnum
from typing import LiteralString

from .._util.doc import robotmesh_doc
from .._util.measurement_with_unit import _MeasurementWithUnitABC


__all__: Sequence[LiteralString] = 'TemperatureUnits', '_Temperature'


@robotmesh_doc("""
    Measurement units for temperature values

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_temperature_units.html
""")
class TemperatureUnits(IntEnum):
    """Temperature units."""

    CELSIUS: int = 0
    FAHRENHEIT: int = 1
    PCT: int = 0xFF


class _Temperature(_MeasurementWithUnitABC):  # pylint: disable=too-few-public-methods
    measurement: float
    unit: TemperatureUnits = TemperatureUnits.CELSIUS
