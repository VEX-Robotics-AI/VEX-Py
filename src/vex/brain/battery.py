"""Brain Battery."""


from collections.abc import Sequence

from abm.decor import sense

from .._abstract_device import SingletonDevice
from ..util.doc import vexcode_doc


__all__: Sequence[str] = ('BrainBattery',)


class BrainBattery(SingletonDevice):
    # pylint: disable=too-few-public-methods
    """Brain Battery."""

    @vexcode_doc("""
        Battery Capacity.

        Reports the charge level of the IQ Brain's battery.

        Battery capacity reports a range from 0 to 100 percent.
    """)
    @sense
    def capacity(self) -> int:
        """Return brain battery capacity as percentage."""
