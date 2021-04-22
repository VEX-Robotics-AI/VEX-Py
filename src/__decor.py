from enum import IntEnum
from functools import wraps
from inspect import getfullargspec
import json
from typing import Any, Callable, TypeVar


CallableTypeVar = TypeVar('CallableTypeVar', bound=Callable[..., Any])


def stringify_device_or_enum(obj: Any):
    from vex.abstract import Device, SingletonDevice   # avoid circ import

    return (str(obj)
            if isinstance(obj, (Device, SingletonDevice, IntEnum))
            else obj)


def args_dict_from_func_and_given_args(func, given_args):
    arg_spec = getfullargspec(func)
    arg_names = arg_spec.args

    args_dict = {arg_names[i]: v for i, v in enumerate(given_args)}
    if (n_defaults_to_use := len(arg_names) - len(given_args)) > 0:
        args_dict.update(
            zip(arg_names[-n_defaults_to_use:],
                arg_spec.defaults[-n_defaults_to_use:]))

    return args_dict


def act(actuating_func: CallableTypeVar) -> CallableTypeVar:
    # (use same signature for IDE code autocomplete to work)

    @wraps(actuating_func)
    def decor_actuating_func(*given_args):
        args_dict = args_dict_from_func_and_given_args(
                        func=actuating_func,
                        given_args=given_args)

        print_args = args_dict.copy()
        self_arg = print_args.pop('self', None)
        input_arg_strs = [f'{k}={stringify_device_or_enum(v)}'
                          for k, v in print_args.items()]
        print((f'ACT: {self_arg}.' if self_arg else 'ACT: ') +
              f"{actuating_func.__name__}({', '.join(input_arg_strs)})")

        return (actuating_func.__qualname__, args_dict)

    return decor_actuating_func


def sense(sensing_func: CallableTypeVar) -> CallableTypeVar:
    # (use same signature for IDE code autocomplete to work)

    sensing_func_name = sensing_func.__name__

    # name of private dict storing current sensing states
    sensing_state_dict_name = f'_{sensing_func_name}'

    @wraps(sensing_func)
    def decor_sensing_func(*given_args, set=None):
        args_dict = args_dict_from_func_and_given_args(
                        func=sensing_func,
                        given_args=given_args)

        # get self
        self = args_dict.pop('self')

        # private dict storing current sensing states
        sensing_state_dict = getattr(self, sensing_state_dict_name, None)
        if sensing_state_dict is None:
            sensing_state_dict = {}
            setattr(self, sensing_state_dict_name, sensing_state_dict)

        # tuple & str forms of input args
        input_arg_dict_items = args_dict.items()
        input_arg_tuple = tuple(input_arg_dict_items)
        input_arg_strs = [f'{k}={stringify_device_or_enum(v)}'
                          for k, v in input_arg_dict_items]

        if set is None:
            return_annotation = sensing_func.__annotations__.get('return')
            return_annotation_str = (f': {return_annotation}'
                                     if return_annotation
                                     else '')
            print_str = (f'SENSE: {self}.{sensing_func_name}'
                         f"({', '.join(input_arg_strs)})"
                         f'{return_annotation_str} = ')

            # if input_arg_tuple is in current sensing states,
            # then pop and return corresponding value
            if input_arg_tuple in sensing_state_dict:
                value = sensing_state_dict.pop(input_arg_tuple)
                print(f'{print_str}{value}')
                return value

            # else ask user for direct input
            else:
                return json.loads(input(f'{print_str}? (in JSON)   '))

        else:
            # set the provided value in current sensing states
            sensing_state_dict[input_arg_tuple] = set
            print(f'SET: {self}.{sensing_state_dict_name}'
                  f"[{', '.join(input_arg_strs)}] = {set}")

    return decor_sensing_func
