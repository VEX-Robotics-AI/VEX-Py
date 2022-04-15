"""Execute script and get State Sequence."""


from collections.abc import Sequence

import click

from __vex.exec import exec_and_get_state_seq as _exec_and_get_state_seq


__all__: Sequence[str] = ('exec_and_get_state_seq',)


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
                shell_complete=None,
                autocompletion=None)
def exec_and_get_state_seq(script_file_path: str):
    """Execute script and get State Sequence."""
    return _exec_and_get_state_seq(script_file_path=script_file_path)
