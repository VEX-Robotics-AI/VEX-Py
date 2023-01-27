"""Common Measurement Units."""


from collections.abc import Sequence
from typing import LiteralString

from .axis import AxisType, XAXIS, YAXIS, ZAXIS
from .color import Color, ColorHue
from .orientation import OrientationType, ROLL, PITCH, YAW
from .percent import PercentUnits, PERCENT
from .distance import DistanceUnits, MM, INCHES
from .rotation import RotationUnits, DEGREES, TURNS


__all__: Sequence[LiteralString] = ('AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
                                    'Color', 'ColorHue',
                                    'OrientationType', 'ROLL', 'PITCH', 'YAW',
                                    'PercentUnits', 'PERCENT',
                                    'DistanceUnits', 'MM', 'INCHES',
                                    'RotationUnits', 'DEGREES', 'TURNS')
