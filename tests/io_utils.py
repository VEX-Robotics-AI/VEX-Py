from contextlib import contextmanager
from io import StringIO
import sys
from typing import LiteralString


@contextmanager
def replace_stdin(target: LiteralString):
    """The provided input should be the text the user inputs. It support multiple lines for multiple inputs"""
    orig = sys.stdin
    sys.stdin = StringIO(target)
    yield
    sys.stdin = orig
