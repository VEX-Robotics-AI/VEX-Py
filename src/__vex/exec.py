"""Execution Utilities."""


from ast import parse, Call, FunctionDef, Module
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

        print('=========')
        print(f'EXECUTING {module_obj_or_script_file_path}...')
        print('---------')

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

    print()
    pprint(object=state_seq,
           stream=None,
           indent=1,
           width=80,
           depth=None,
           compact=False,
           sort_dicts=False,
           # underscore_numbers=True,   # Py3.10
           )
    print()

    return state_seq


def compare_output(script_file_paths: tuple[str, str],
                   func_name: Optional[str] = None,
                   context_file_path: Optional[str] = None,
                   func_args: Optional[Union[dict, list, tuple]] = None) -> bool:   # noqa: E501
    # pylint: disable=too-many-locals
    """Compare output of 2 functions or scripts."""
    script_file_path_0, script_file_path_1 = script_file_paths

    if func_name:
        with open(file=script_file_path_0,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            module_0: Module = parse(source=f.read(),
                                     filename=script_file_path_0,
                                     mode='exec',
                                     type_comments=False,
                                     feature_version=None)
            try:
                func_def_0: FunctionDef = next(i for i in module_0.body
                                               if isinstance(i, FunctionDef)
                                               and i.name == func_name)   # noqa: E501,W503
            except StopIteration as err:
                raise ValueError(f'*** {script_file_path_0} HAS NO '
                                 f'`def {func_name}(...)` ***') from err

        with open(file=script_file_path_1,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            module_1: Module = parse(source=f.read(),
                                     filename=script_file_path_1,
                                     mode='exec',
                                     type_comments=False,
                                     feature_version=None)
            try:
                func_def_1: FunctionDef = next(i for i in module_1.body
                                               if isinstance(i, FunctionDef)
                                               and i.name == func_name)   # noqa: E501,W503
            except StopIteration as err:
                raise ValueError(f'*** {script_file_path_1} HAS NO '
                                 f'`def {func_name}(...)` ***') from err

        assert context_file_path, \
            '*** context_file_path IS REQUIRED TO CHECK FUNCTION EQUALITY ***'
        with open(file=context_file_path,
                  mode='rt',
                  buffering=-1,
                  encoding='utf-8',
                  errors='strict',
                  newline=None,
                  closefd=True,
                  opener=None) as f:
            module: Module = parse(source=f.read(),
                                   filename=script_file_path_1,
                                   mode='exec',
                                   type_comments=False,
                                   feature_version=None)

        if func_args:
            with open(file=context_file_path,
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

        return Call(module, func_def_0, func_def_1)

    print(result := (
        exec_and_get_state_seq(module_obj_or_script_file_path=script_file_path_0) ==   # noqa: E501
        exec_and_get_state_seq(module_obj_or_script_file_path=script_file_path_1)   # noqa: E501
    ))

    return result
