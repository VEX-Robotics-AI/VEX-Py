"""Execute script and get State Sequence."""


from ast import Module
from collections.abc import Sequence
from pprint import pprint
from typing import Union

import __vex.decor


__all__: Sequence[str] = ('exec_and_get_state_seq',)


def exec_and_get_state_seq(
        module_obj_or_script_file_path: Union[str, Module]) -> list:
    """Execute Module object or script and get State Sequence."""
    if isinstance(module_obj_or_script_file_path, str):
        with open(file=module_obj_or_script_file_path,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            exec(f.read())   # pylint: disable=exec-used

    else:
        exec(module_obj_or_script_file_path)   # pylint: disable=exec-used

    state_seq: list = __vex.decor.STATE_SEQ
    __vex.decor.STATE_SEQ = []

    pprint(object=state_seq,
           stream=None,
           indent=1,
           width=80,
           depth=None,
           compact=False,
           sort_dicts=False,
           # underscore_numbers=True,   # Py3.10
           )

    return state_seq
