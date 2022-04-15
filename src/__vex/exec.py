"""Execution Utilities."""


from ast import parse, FunctionDef, Module
from collections.abc import Sequence
import json
from pprint import pprint
from typing import Optional, Union

import __vex.decor


__all__: Sequence[str] = ('exec_and_get_state_seq',)


def exec_and_get_state_seq(
        module_obj_or_script_file_path: Union[Module, str]) -> list:
    """Execute Module object or script and get State Sequence."""
    if isinstance(module_obj_or_script_file_path, Module):
        exec(module_obj_or_script_file_path)   # pylint: disable=exec-used

    else:
        assert isinstance(module_obj_or_script_file_path, str)

        with open(file=module_obj_or_script_file_path,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            exec(f.read())   # pylint: disable=exec-used

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


def compare_output(scripts: tuple[str, str],
                   func: Optional[str] = None,
                   context_file: Optional[str] = None,
                   func_args: Optional[str] = None):
    """Compare output of 2 functions or scripts."""
    script_file_path_0, script_file_path_1 = scripts

    with open(file=script_file_path_0,
              mode='rt',
              buffering=-1,
              encoding='utf-8',
              errors='strict',
              newline=None,
              closefd=True,
              opener=None) as f:
        code_str_0: str = f.read()

    with open(file=script_file_path_1,
              mode='rt',
              buffering=-1,
              encoding='utf-8',
              errors='strict',
              newline=None,
              closefd=True,
              opener=None) as f:
        code_str_1: str = f.read()

    if func:
        code_0: Module = parse(source=code_str_0,
                               filename=script_file_path_0,
                               mode='exec',
                               type_comments=False,
                               feature_version=None)
        try:
            func_code_0: FunctionDef = next(i for i in code_0.body
                                            if isinstance(i, FunctionDef)
                                            and i.name == func)   # noqa: W503
        except StopIteration as err:
            raise ValueError(f'*** {script_file_path_0} HAS NO '
                             f'`def {func}(...)` ***') from err

        code_1: Module = parse(source=code_str_1,
                               filename=script_file_path_1,
                               mode='exec',
                               type_comments=False,
                               feature_version=None)
        try:
            func_code_1: FunctionDef = next(i for i in code_1.body
                                            if isinstance(i, FunctionDef)
                                            and i.name == func)   # noqa: W503
        except StopIteration as err:
            raise ValueError(f'*** {script_file_path_1} HAS NO '
                             f'`def {func}(...)` ***') from err

        print(func_code_0, func_code_1)

        if context_file:
            with open(file=context_file,
                      mode='rt',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as f:
                _: str = f.read()

        if func_args:
            with open(file=context_file,
                      mode='rt',
                      buffering=-1,
                      encoding='utf-8',
                      errors='strict',
                      newline=None,
                      closefd=True,
                      opener=None) as f:
                func_args: Union[dict, list] = json.loads(s=func_args,
                                                          cls=None,
                                                          object_hook=None,
                                                          parse_float=None,
                                                          parse_int=None,
                                                          parse_constant=None,
                                                          object_pairs_hook=None)   # noqa: E501

    else:
        print(script_file_path_0, script_file_path_1)
