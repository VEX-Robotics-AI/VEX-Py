from enum import IntEnum
from functools import wraps
from inspect import getfullargspec, getmembers, isclass, isfunction
from typing import Any, Callable, TypeVar


CallableTypeVar = TypeVar('CallableTypeVar', bound=Callable[..., Any])


def stringify_device_or_enum(obj: Any):
    from vex.abstract import Device, DeviceWithoutPort   # avoid circ import

    return (str(obj)
            if isinstance(obj, (Device, DeviceWithoutPort, IntEnum))
            else obj)


def return_qualname_and_args(cls_or_func: CallableTypeVar) -> CallableTypeVar:
    # (use same signature for IDE code autocomplete to work)

    @wraps(cls_or_func)
    def decor_func(*given_args):
        arg_spec = getfullargspec(cls_or_func)
        arg_names = arg_spec.args

        args_dict = {arg_names[i]: stringify_device_or_enum(v)
                     for i, v in enumerate(given_args)}
        if (n_defaults_to_use := len(arg_names) - len(given_args)):
            args_dict.update(
                zip(arg_names[-n_defaults_to_use:],
                    map(stringify_device_or_enum,
                        arg_spec.defaults[-n_defaults_to_use:])))

        result = (cls_or_func.__qualname__, args_dict)
        print(result)
        return result

    if isfunction(cls_or_func):
        return decor_func

    else:
        assert isclass(cls_or_func)

        for method_name, method in getmembers(cls_or_func, isfunction):
            if not method_name.startswith('_'):
                setattr(cls_or_func, method_name,
                        return_qualname_and_args(method))

        return cls_or_func
