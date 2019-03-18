#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
from functools import wraps


def singleton(cls):
    """
    >>> @singleton
    ... class A:
    ...     pass
    >>> id(A()) == id(A()) == id(A())
    True
    """
    instances = {}

    @wraps(cls)
    def Singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return Singleton


if __name__ == "__main__":
    import doctest
    doctest.testmod()
