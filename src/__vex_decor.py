"""Decorators."""


from collections.abc import Sequence
from enum import IntEnum
from functools import wraps
from inspect import FullArgSpec, getfullargspec
import json
from typing import Any, Callable, Optional, TypeVar
import re


__all__: Sequence[str] = 'act', 'sense'


_OBJECT_MEMORY_PATTERN: str = ' object at 0x([0-9]|[a-f]|[A-F])+'
CallableTypeVar = TypeVar('CallableTypeVar', bound=Callable[..., Any])


def stringify_device_or_enum(obj: Any) -> str:
    """Stringify device or enum."""
    # pylint: disable=import-outside-toplevel
    from vex.abstract import Device, SingletonDevice   # avoid circular import

    return (str(obj)
            if isinstance(obj, (Device, SingletonDevice, IntEnum))
            else (f'"{obj}"'
                  if isinstance(obj, str)
                  else obj))


def args_dict_from_func_and_given_args(func: CallableTypeVar,
                                       given_args: Sequence[Any]) -> dict[str, Any]:   # noqa: E501
    """Get arguments dict from function and given arguments."""
    arg_spec: FullArgSpec = getfullargspec(func)
    arg_names: list[str] = arg_spec.args

    args_dict: dict[str, Any] = {arg_names[i]: v for i, v in enumerate(given_args)}   # noqa: E501
    if (n_defaults_to_use := len(arg_names) - len(given_args)) > 0:
        args_dict.update(zip(arg_names[-n_defaults_to_use:],
                             arg_spec.defaults[-n_defaults_to_use:]))

    return args_dict


def sanitize_object_name(obj: Any) -> Optional[str]:
    """Sanitize object name."""
    return (None
            if obj is None
            else re.sub(_OBJECT_MEMORY_PATTERN, '', str(obj)))


def act(actuating_func: CallableTypeVar) -> CallableTypeVar:
    """Actuation decorator."""
    # (use same signature for IDE code autocomplete to work)

    @wraps(actuating_func)
    def decor_actuating_func(*given_args) -> tuple[str, dict[str, Any]]:
        args_dict: dict[str, Any] = \
            args_dict_from_func_and_given_args(func=actuating_func,
                                               given_args=given_args)

        print_args: dict[str, Any] = args_dict.copy()
        self_arg: Optional[Any] = print_args.pop('self', None)
        input_arg_strs: list[str] = [f'{k}={stringify_device_or_enum(v)}'
                                     for k, v in print_args.items()]
        self_name: Optional[str] = sanitize_object_name(self_arg)
        print((f'ACT: {self_name}.' if self_name else 'ACT: ') +
              f"{actuating_func.__name__}({', '.join(input_arg_strs)})")

        return actuating_func.__qualname__, args_dict

    return decor_actuating_func


def sense(sensing_func: CallableTypeVar) -> CallableTypeVar:
    """Sensing decorator."""
    # (use same signature for IDE code autocomplete to work)

    # name of private dict storing current sensing states
    sensing_state_dict_name: str = f'_{(sensing_func_name := sensing_func.__name__)}'   # noqa: E501

    @wraps(sensing_func)
    def decor_sensing_func(*given_args, set=None):
        # pylint: disable=import-outside-toplevel,redefined-builtin
        from vex import interactive

        args_dict: dict[str, Any] = \
            args_dict_from_func_and_given_args(func=sensing_func,
                                               given_args=given_args)

        # get self
        self: Any = args_dict.pop('self')

        # private dict storing current sensing states
        if (sensing_state_dict :=
            getattr(self, sensing_state_dict_name, None)) is None:   # noqa: E129,E501
            setattr(self, sensing_state_dict_name, (sensing_state_dict := {}))

        # tuple & str forms of input args
        input_arg_tuple: tuple[tuple[str, Any], ...] = \
            tuple(input_arg_dict_items := args_dict.items())
        input_arg_strs: list[str] = [f'{k}={stringify_device_or_enum(v)}'
                                     for k, v in input_arg_dict_items]

        if set is None:
            return_annotation: Optional[type] = \
                sensing_func.__annotations__.get('return')
            return_annotation_str: str = (f': {return_annotation}'
                                          if return_annotation
                                          else '')
            print_str: str = (f'SENSE: {self}.{sensing_func_name}'
                              f"({', '.join(input_arg_strs)})"
                              f'{return_annotation_str} = ')

            # if input_arg_tuple is in current sensing states,
            # then get and return corresponding value
            if input_arg_tuple in sensing_state_dict:
                value = sensing_state_dict.get(input_arg_tuple)
                if isinstance(value, list):
                    if len(value) == 0:
                        return None
                    return_value = value[0]
                    sensing_state_dict[input_arg_tuple] = value[1:]
                else:
                    return_value = value
                print(f'{print_str}{return_value}')
                return return_value

            # else if interactive.ON, ask user for direct input
            if interactive.ON:
                return json.loads(input(f'{print_str}? (in JSON)   '))

            # else return default sensing result
            return sensing_func(*given_args)

        # else: set the provided value in current sensing states
        sensing_state_dict[input_arg_tuple] = set
        print(f'SET: {self}.{sensing_state_dict_name}'
              f"[{', '.join(input_arg_strs)}] = {set}")
        return None

    return decor_sensing_func
