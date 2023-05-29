"""Brain Battery."""


from collections.abc import Sequence
from typing import LiteralString, Self

from abm.decor import sense

from .._device import SingletonDevice

from .._util.doc import vexcode_doc


__all__: Sequence[LiteralString] = ('BrainBattery',)


class BrainBattery(SingletonDevice):
    # pylint: disable=too-few-public-methods
    """Brain Battery."""

    @vexcode_doc("""
        Battery Capacity.

        Reports the charge level of the IQ Brain's battery.

        Battery capacity reports a range from 0 to 100 percent.
    """)
    @sense
    def capacity(self: Self) -> int:
        """Return brain battery capacity as percentage."""
