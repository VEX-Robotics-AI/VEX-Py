"""Robot Mesh VEX CLI."""


import click

from .inspect_class import inspect_robotmesh_vex_class


@click.group(name='h1st',
             cls=click.Group,
             commands={
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
