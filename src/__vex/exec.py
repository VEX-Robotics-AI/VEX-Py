"""Execution Utilities."""


from ast import (
    Name, Load, Store,
    Assign, Attribute, Call, Constant, Expr, FunctionDef, ImportFrom, Module,
    alias, fix_missing_locations, parse, unparse,
)
from collections.abc import Sequence
from copy import deepcopy
from pathlib import Path
from pprint import pprint
from typing import Optional, Union

import __vex.decor


__all__: Sequence[str] = 'exec_and_get_state_seq', 'compare_output'


def exec_and_get_state_seq(
        module_obj_or_script_file_path: Union[Module, Path, str]) -> list:
    """Execute Module object or script and get State Sequence."""
    # pylint: disable=exec-used

    if isinstance(module_obj_or_script_file_path, Module):
        print('========================')
        print('EXECUTING CODE MODULE...')
        print('------------------------')
        print(code_str :=   # bugs.python.org/issue44896
              unparse(ast_obj=fix_missing_locations(module_obj_or_script_file_path)))   # noqa: E501
        print('------------------------')

        exec(code_str, globals())

    else:
        assert isinstance(module_obj_or_script_file_path, (Path, str))

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
            exec(f.read())

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


def _name_or_attr_from_str(s: str, /) -> Union[Name, Attribute]:
    str_components = s.split(sep='.', maxsplit=1)

    if len(str_components) == 1:
        return Name(id=str_components[0], ctx=Load())

    assert len(str_components) == 2
    name, attr_name = str_components
    return Attribute(value=Name(id=name, ctx=Load()), attr=attr_name, ctx=Load())   # noqa: E501


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
            context_module: Module = parse(source=f.read(),
                                           filename=context_file_path,
                                           mode='exec',
                                           type_comments=False,
                                           feature_version=None)

        if func_args:
            func_args: list = [(_name_or_attr_from_str(arg_value[1:-1])
                                if isinstance(arg_value, str) and
                                arg_value.startswith('`') and
                                arg_value.endswith('`')
                                else Constant(value=arg_value))
                               for arg_value in (func_args.values()
                                                 if isinstance(func_args, dict)
                                                 else func_args)]

        else:
            func_args: list = []

        decor_import: ImportFrom = ImportFrom(module='__vex.decor',
                                              names=[alias(name=(decor_name :=
                                                                 'sense'),
                                                           asname=None)],
                                              level=0)

        func_decor: Assign = Assign(targets=[Name(id=func_name, ctx=Store())],
                                    value=Call(func=Name(id=decor_name,
                                                         ctx=Load()),
                                               args=[Name(id=func_name,
                                                          ctx=Load())],
                                               keywords=[],
                                               starargs=[],
                                               kwargs=[]),
                                    type_comment=None)

        func_call: Expr = Expr(value=Call(func=Name(id=func_name, ctx=Load()),
                                          args=func_args, keywords=[],
                                          starargs=[], kwargs=[]))

        module_0: Module = deepcopy(context_module)
        module_0.body.extend((func_def_0, decor_import, func_decor, func_call))

        module_1: Module = deepcopy(context_module)
        module_1.body.extend((func_def_1, decor_import, func_decor, func_call))

        result: bool = (
            exec_and_get_state_seq(module_obj_or_script_file_path=module_0) ==
            exec_and_get_state_seq(module_obj_or_script_file_path=module_1)
        )

    else:
        result: bool = (
            exec_and_get_state_seq(
                module_obj_or_script_file_path=script_file_path_0) ==
            exec_and_get_state_seq(
                module_obj_or_script_file_path=script_file_path_1)
        )

    print(result)
    return result
