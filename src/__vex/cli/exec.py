"""Execution Utilities."""


from collections.abc import Sequence
import json
from typing import Optional, Union

import click

from __vex.exec import (exec_and_get_state_seq as _exec_and_get_state_seq,
                        compare_output as _compare_output)


__all__: Sequence[str] = 'exec_and_get_state_seq', 'compare_output'


@click.command(name='exec',
               cls=click.Command,

               # Command kwargs
               context_settings=None,
               # callback=None,
               # params=None,
               help='Execute script and get State Sequence >>>',
               epilog='^^^ Execute script and get State Sequence',
               short_help='Execute script and get State Sequence',
               options_metavar='[OPTIONS]',
               add_help_option=True,
               no_args_is_help=True,
               hidden=False,
               deprecated=False)
@click.argument('script_file_path',
                type=str,
                required=True,
                default=None,
                callback=None,
                nargs=None,
                # multiple=False,
                metavar='SCRIPT_FILE_PATH',
                expose_value=True,
                is_eager=False,
                envvar=None,
                shell_complete=None)
def exec_and_get_state_seq(script_file_path: str):
    """Execute script and get State Sequence."""
    return _exec_and_get_state_seq(module_obj_or_script_file_path=script_file_path)   # noqa: E501


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
                shell_complete=None)
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
              shell_complete=None)
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
              shell_complete=None)
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
              shell_complete=None)
def compare_output(scripts: tuple[str, str],
                   func: Optional[str] = None,
                   context_file: Optional[str] = None,
                   func_args: Optional[str] = None):
    """Compare output of 2 functions or scripts."""
    if func_args:
        func_args: Union[dict, list] = json.loads(s=func_args,
                                                  cls=None,
                                                  object_hook=None,
                                                  parse_float=None,
                                                  parse_int=None,
                                                  parse_constant=None,
                                                  object_pairs_hook=None)

    return _compare_output(script_file_paths=scripts,
                           func_name=func,
                           context_file_path=context_file,
                           func_args=func_args)
