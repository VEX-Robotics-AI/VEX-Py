"""Robot Mesh VEX CLI."""


from collections.abc import Sequence

import click

from .exec import exec_and_get_state_seq, compare_output
from .inspect_class import inspect_robotmesh_vex_class


__all__: Sequence[str] = ('robotmesh_vex_cli',)


@click.group(name='h1st',
             cls=click.Group,
             commands={
                 'exec': exec_and_get_state_seq,
                 'compare-output': compare_output,
                 'inspect-cls': inspect_robotmesh_vex_class,
             },

             # Command kwargs
             context_settings=None,
             # callback=None,
             # params=None,
             help='Robot Mesh VEX CLI >>>',
             epilog='^^^ Robot Mesh VEX CLI',
             short_help='Robot Mesh VEX CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             no_args_is_help=True,
             hidden=False,
             deprecated=False,

             # Group/MultiCommand kwargs
             invoke_without_command=False,
             subcommand_metavar='ROBOTMESH_VEX_SUB_COMMAND',
             chain=False,
             result_callback=None)
def robotmesh_vex_cli():
    """Robot Mesh VEX CLI."""
