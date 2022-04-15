"""Execute script and get State Sequence."""


from collections.abc import Sequence
from pprint import pprint

import click

import __vex.decor


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
    with open(file=script_file_path,
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
