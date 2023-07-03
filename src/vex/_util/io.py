from contextlib import contextmanager
from io import StringIO
import sys
from typing import LiteralString


@contextmanager
def replace_stdin(target: LiteralString):
    """Replace stdin input by user with this string.

    Multiple lines for multiple inputs are supported.
    """
    orig = sys.stdin
    sys.stdin = StringIO(target)
    yield
    sys.stdin = orig
