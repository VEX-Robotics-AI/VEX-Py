"""Common Measurement Units."""


from collections.abc import Sequence
from typing import LiteralString

from .analog import AnalogUnits
from .axis import AxisType, XAXIS, YAXIS, ZAXIS
from .color import Color, ColorHue
from .distance import DistanceUnits, MM, INCHES
from .orientation import OrientationType, ROLL, PITCH, YAW
from .percent import PercentUnits, PERCENT
from .power import PowerUnits
from .rotation import RotationUnits, DEGREES, TURNS
from .velocity import VelocityUnits, RPM, DPS


__all__: Sequence[LiteralString] = ('AnalogUnits',
                                    'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
                                    'Color', 'ColorHue',
                                    'DistanceUnits', 'MM', 'INCHES',
                                    'OrientationType', 'ROLL', 'PITCH', 'YAW',
                                    'PercentUnits', 'PERCENT',
                                    'PowerUnits',
                                    'RotationUnits', 'DEGREES', 'TURNS',
                                    'VelocityUnits', 'RPM', 'DPS')
