"""Compare output of 2 functions or scripts."""


from typing import Optional

import click


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
def compare_output(context_file: Optional[str] = None):
    """Compare output of 2 functions or scripts."""
    if context_file:
        # pylint: disable=exec-used,unspecified-encoding
        exec(open(context_file).read())
