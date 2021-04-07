from inspect import getfullargspec, getmembers, isclass, isfunction
from typing import Any, Callable, TypeVar


CallableTypeVar = TypeVar('CallableTypeVar', bound=Callable[..., Any])


def return_qualname_and_args(cls_or_func: CallableTypeVar) -> CallableTypeVar:
    # (use same signature for IDE code autocomplete to work)

    def decor_func(*given_args):
        arg_spec = getfullargspec(cls_or_func)
        arg_names = arg_spec.args
        n_defaults_to_use = len(arg_names) - len(given_args)
        result = (cls_or_func.__qualname__,
                  {arg_names[i]: v for i, v in enumerate(given_args)} |
                  dict(zip(arg_names[-n_defaults_to_use:],
                           arg_spec.defaults[-n_defaults_to_use:])))
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
