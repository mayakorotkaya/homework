#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Wraps:
    """
    >>> def decorator(func):
    ...     @wraps(func)
    ...     def wrapper(*args, **kwargs):
    ...         return func(*args, **kwargs)
    ...     return wrapper
    >>> @decorator
    ... def foo(x):
    ...     \"\"\"Docstring foo\"\"\"
    ...     return x
    >>> foo("test")
    'test'
    >>> foo.__doc__
    'Docstring foo'
    >>> foo.__name__
    'foo'
    >>> foo.__module__
    '__main__'
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, wrapper):
        wrapper.__doc__ = self.func.__doc__
        wrapper.__name__ = self.func.__name__
        wrapper.__module__ = self.func.__module__
        return wrapper


wraps = Wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator
def foo(x):
    """Docstring foo"""
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
