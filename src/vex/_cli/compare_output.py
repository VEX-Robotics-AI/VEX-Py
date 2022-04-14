"""Compare output of 2 functions or scripts."""


from ast import parse, FunctionDef, Module
from collections.abc import Sequence
from typing import Optional, Tuple

import click


__all__: Sequence[str] = ('compare_output',)


@click.command(name='compare-output',
               cls=click.Command,

               # Command kwargs
               context_settings=None,
               # callback=None,
               # params=None,
               help='Compare output of 2 functions or scripts >>>',
               epilog='^^^ Compare output of 2 functions or scripts',
               short_help='Compare output of 2 functions or scripts',
               options_metavar='[OPTIONS]',
               add_help_option=True,
               no_args_is_help=True,
               hidden=False,
               deprecated=False)
@click.argument('scripts',
                type=str,
                required=True,
                default=None,
                callback=None,
                nargs=2,
                # multiple=False,
                metavar='SCRIPT_FILES',
                expose_value=True,
                is_eager=False,
                envvar=None,
                shell_complete=None,
                autocompletion=None)
@click.option('--func',
              show_default=True,
              prompt=False,
              confirmation_prompt=False,
              prompt_required=True,
              hide_input=False,
              is_flag=False,
              flag_value=None,
              multiple=False,
              count=False,
              allow_from_autoenv=True,
              help='Function Name',
              hidden=False,
              show_choices=True,
              show_envvar=False,

              type=str,
              required=False,
              default=None,
              callback=None,
              nargs=None,
              # multiple=False,
              metavar='FUNCTION_NAME',
              expose_value=True,
              is_eager=False,
              envvar=None,
              shell_complete=None,
              autocompletion=None)
@click.option('--context-file',
              show_default=True,
              prompt=False,
              confirmation_prompt=False,
              prompt_required=True,
              hide_input=False,
              is_flag=False,
              flag_value=None,
              multiple=False,
              count=False,
              allow_from_autoenv=True,
              help='Context File Path',
              hidden=False,
              show_choices=True,
              show_envvar=False,

              type=str,
              required=False,
              default=None,
              callback=None,
              nargs=None,
              # multiple=False,
              metavar='CONTEXT_FILE_PATH',
              expose_value=True,
              is_eager=False,
              envvar=None,
              shell_complete=None,
              autocompletion=None)
@click.option('--func-args',
              show_default=True,
              prompt=False,
              confirmation_prompt=False,
              prompt_required=True,
              hide_input=False,
              is_flag=False,
              flag_value=None,
              multiple=False,
              count=False,
              allow_from_autoenv=True,
              help='Function Arguments',
              hidden=False,
              show_choices=True,
              show_envvar=False,

              type=str,
              required=False,
              default=None,
              callback=None,
              nargs=None,
              # multiple=False,
              metavar='FUNCTION_ARGUMENTS',
              expose_value=True,
              is_eager=False,
              envvar=None,
              shell_complete=None,
              autocompletion=None)
def compare_output(scripts: Tuple[str, str],
                   func: Optional[str] = None,
                   context_file: Optional[str] = None):
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

    else:
        print(script_file_path_0, script_file_path_1)
