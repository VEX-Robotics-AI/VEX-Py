"""Time."""


from collections.abc import Sequence
from typing import overload

from abm.decor import act

from .units import TimeUnits, SECONDS, MSEC

from .._util.doc import robotmesh_doc, vexcode_doc
from .._util.type import NumType


__all__: Sequence[str] = 'TimeUnits', 'SECONDS', 'MSEC', 'clock', 'wait'


@robotmesh_doc("""
    Get the number of seconds since system startup.
""")
def clock() -> NumType:
    """Return number of seconds since program started."""


@overload
def wait(duration: NumType, unit: TimeUnits = MSEC, /):
    ...


@overload
def wait(time: NumType, timeUnits: TimeUnits = TimeUnits.SEC, /):
    ...


@robotmesh_doc("""
    Wait for a specific amount of time.

    Identical to sys.sleep().

    Parameters
    - time: The length of time to wait
    - timeUnits: The units of time (default seconds)

    robotmesh.com/studio/content/docs/vexiq-python_b/html/namespacevex.html#a6b9ca2db773bef3a3569a0d6b22f2749
""")
@vexcode_doc("""
    Waits for a specific amount of time before moving to the next command.

    Set an amount of time in SECONDS or MSEC on the UNITS parameter
    to have your program wait before executing subsequent commands.
""")
@act
def wait(duration: NumType, unit: TimeUnits = SECONDS, /):
    # pylint: disable=unused-argument
    """Wait for specified duration."""
