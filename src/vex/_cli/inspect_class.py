"""Inspect a Robot Mesh VEX class's methods and their return types."""


from collections.abc import Sequence
from importlib import import_module
from inspect import (getfullargspec, getmembers,
                     isdatadescriptor, isfunction,
                     signature)
from types import ModuleType
from typing import Optional

import click


__all__: Sequence[str] = ('inspect_robotmesh_vex_class',)


@click.command(name='inspect-cls',
               cls=click.Command,

               # Command kwargs
               context_settings=None,
               # callback=None,
               # params=None,
               help='Inspect a Robot Mesh VEX Class >>>',
               epilog='^^^ Inspect a Robot Mesh VEX Class',
               short_help='Inspect a Robot Mesh VEX Class',
               options_metavar='[OPTIONS]',
               add_help_option=True,
               no_args_is_help=True,
               hidden=False,
               deprecated=False)
@click.argument('class_qualname',
                type=str,
                required=True,
                default=None,
                callback=None,
                nargs=None,
                # multiple=False,
                metavar='CLASS_QUALNAME',
                expose_value=True,
                is_eager=False,
                envvar=None,
                shell_complete=None,
                autocompletion=None)
def inspect_robotmesh_vex_class(class_qualname: str):
    """Inspect a Robot Mesh VEX class's methods and their return types."""
    print(class_qualname)

    module_name, class_name = class_qualname.rsplit('.', 1)
    module: ModuleType = import_module(name=module_name)
    cls: type = getattr(module, class_name)

    print('\nProperties:')
    for pty_name, pty in getmembers(cls, isdatadescriptor):
        if not pty_name.startswith('_'):
            return_annotation: Optional[type] = pty.fget.__annotations__.get('return')  # noqa: E501
            print(f'- {pty_name}: {return_annotation}'
                  if return_annotation
                  else f'- {pty_name}')

    print('\nMethods:')
    for method_name, method in getmembers(cls, isfunction):
        print(f'\n- {method_name}{signature(method)}:'
              f'\n    {getfullargspec(method)}')
