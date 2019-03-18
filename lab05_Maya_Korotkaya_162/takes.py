#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


class Takes:
    """
    >>> @Takes(int, str, float, int)
    ... def foo(*args):
    ...     print(args)
    >>> try:
    ...     args = 1, "arg1", 2.0, 11
    ...     foo(*args)
    ... except TypeError as exc:
    ...     print(str(exc))
    (1, 'arg1', 2.0, 11)
    >>> @Takes(int, float, str, int)
    ... def bar(*args):
    ...     print(args)
    >>> try:
    ...     args = 1, "arg1", "kek", 12.0
    ...     foo(*args)
    ... except TypeError as exc:
    ...     print(str(exc))
    str argument in position 2 is not float object
    """
    def __init__(self, *args):
        self.types = args

    def __call__(self, func):
        types = self.types

        @functools.wraps(func)
        def wrapper(*fargs):
            for i, (arg, type_) in enumerate(zip(fargs, types)):
                if not isinstance(arg, type_):
                    raise TypeError(f"{type(arg).__name__} argument"
                                    f" in position {i} is not"
                                    f" {type_.__name__} object")
            return func(*fargs)
        return wrapper


takes = Takes


if __name__ == "__main__":
    import doctest
    doctest.testmod()
