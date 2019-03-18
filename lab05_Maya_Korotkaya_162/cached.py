#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def cached(func):  # correct signature is not known
    """
    >>> @cached
    ... def add(a, b):
    ...     print(a, b)
    ...     return a + b
    ...
    >>> add(1, 2)
    1 2
    3
    >>> add(1, 2)
    3
    >>> add(2, 2)
    2 2
    4
    >>> add(2, 2)
    4
    """
    cach = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        kwargs_key = tuple(sorted(kwargs.items(), key=lambda x: x[0]))
        full_args_key = (args, kwargs_key)

        if full_args_key not in cach:
            result = func(*args, **kwargs)
            cach[full_args_key] = result
        return cach[full_args_key]
        # if args not in cach:
        #     cach[args] = func(args)
        # return cach[args]
    return wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()
