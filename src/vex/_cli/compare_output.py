"""Compare output of 2 functions or scripts."""


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
@click.argument('files',
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
def compare_output(files: Tuple[str, str],
                   func: Optional[str] = None,
                   context_file: Optional[str] = None):
    """Compare output of 2 functions or scripts."""
    script_file_path_0, script_file_path_1 = files

    if func:
        if context_file:
            # pylint: disable=consider-using-with
            # pylint: disable=exec-used
            # pylint: disable=unspecified-encoding
            exec(open(context_file).read())

    else:
        print(script_file_path_0, script_file_path_1)
