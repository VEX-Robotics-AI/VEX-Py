"""Common Measurement Units."""


from collections.abc import Sequence
from typing import LiteralString

from .analog import AnalogUnits
from .axis import AxisType, XAXIS, YAXIS, ZAXIS
from .color import Color, ColorHue
from .orientation import OrientationType, ROLL, PITCH, YAW
from .percent import PercentUnits, PERCENT
from .distance import DistanceUnits, MM, INCHES
from .rotation import RotationUnits, DEGREES, TURNS
from .velocity import VelocityUnits, RPM, DPS


__all__: Sequence[LiteralString] = ('AnalogUnits',
                                    'AxisType', 'XAXIS', 'YAXIS', 'ZAXIS',
                                    'Color', 'ColorHue',
                                    'OrientationType', 'ROLL', 'PITCH', 'YAW',
                                    'PercentUnits', 'PERCENT',
                                    'DistanceUnits', 'MM', 'INCHES',
                                    'RotationUnits', 'DEGREES', 'TURNS',
                                    'VelocityUnits', 'RPM', 'DPS')
