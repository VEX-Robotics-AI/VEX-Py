"""VEX Distance Sensor."""

from collections.abc import Sequence

from .sonar import Sonar
from .object_size_type import ObjectSizeType

__all__: Sequence[str] = ("Sonar", "ObjectSizeType")
