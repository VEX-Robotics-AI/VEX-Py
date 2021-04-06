from inspect import ismethod, isfunction


def return_qualname_and_args(func):
    def decor_func(*args):
        d = func.__annotations__.copy()
        n_args = len(d)
        print(func, ismethod(func), isfunction(func))

        if len(args) == n_args:   # if normal function
            return (func.__qualname__,
                    {k: args[i] for i, k in enumerate(d)})

        else:
            assert len(args) == n_args + 1   # else must be class method
            return (func.__qualname__,
                    {k: args[i + 1] for i, k in enumerate(d)})

    return decor_func
