"""Compare output of 2 functions or scripts."""


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
def compare_output():
    """Compare output of 2 functions or scripts."""
