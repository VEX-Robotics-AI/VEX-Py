"""Time."""


from collections.abc import Sequence

from abm.decor import act

# pylint: disable=unused-import
from ..util.doc import robotmesh_doc, vexcode_doc   # noqa: F401

from .time_units import TimeUnits


__all__: Sequence[str] = 'TimeUnits', 'wait'


# pylint: disable=unused-argument
@robotmesh_doc("""
    Wait for a specific amount of time.

    Identical to sys.sleep().

    Parameters
    time: The length of time to wait
    timeUnits: The units of time (default seconds)

    robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html#a6b9ca2db773bef3a3569a0d6b22f2749
""")
@act
def wait(time: float, timeUnits: TimeUnits = TimeUnits.SEC, /):
    """Wait."""
