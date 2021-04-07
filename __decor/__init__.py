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

    args_dict = {arg_names[i]: stringify_device_or_enum(v)
                 for i, v in enumerate(given_args)}
    if (n_defaults_to_use := len(arg_names) - len(given_args)) > 0:
        args_dict.update(
            zip(arg_names[-n_defaults_to_use:],
                map(stringify_device_or_enum,
                    arg_spec.defaults[-n_defaults_to_use:])))

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
        input_arg_strs = [f'{k}={v}' for k, v in print_args.items()]
        print(('ACT: ' if self_arg is None else f'ACT: {self_arg}.') +
              f"{actuating_func.__name__}({', '.join(input_arg_strs)})")

        return (actuating_func.__qualname__, args_dict)

    return decor_actuating_func


def sense(sensing_func: CallableTypeVar) -> CallableTypeVar:
    # (use same signature for IDE code autocomplete to work)

    @wraps(sensing_func)
    def decor_sensing_func(*given_args):
        args_dict = args_dict_from_func_and_given_args(
                        func=sensing_func,
                        given_args=given_args)
        self_arg = args_dict.pop('self')
        input_arg_strs = [f'{k}={v}' for k, v in args_dict.items()]
        return json.loads(input(f'SENSE: {self_arg}.{sensing_func.__name__}'
                                f"({', '.join(input_arg_strs)}) = ?   "))

    return decor_sensing_func
