import sys
from io import StringIO
from contextlib import contextmanager


@contextmanager
def replace_stdin(target: str):
    """The provided input should be the text the user inputs. It support multiple lines for multiple inputs"""
    orig = sys.stdin
    sys.stdin = StringIO(target)
    yield
    sys.stdin = orig
