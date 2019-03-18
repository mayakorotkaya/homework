#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minimum(*args, **kwargs):
    """
    The same as built-in min (exclude default parameter).
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    >>> minimum(1, 2, 3) == min(1, 2, 3)
    True
    >>> minimum([1, 2, 3]) == min([1, 2, 3])
    True
    """

    if len(args) > 1:
        it = iter(args)
    else:
        it = iter(args[0])
    least = next(it)
    for i in it:
        if i < least:
            least = i
        for key, value in kwargs.items():
            if value(i) < value(least):
                least = i
    return least


def maximum(*args, **kwargs):
    """
    The same as built-in max (exclude default parameter).
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    >>> maximum(1, 2, 3) == max(1, 2, 3)
    True
    >>> maximum([1, 2, 3]) == max([1, 2, 3])
    True
    """
    if len(args) > 1:
        it = iter(args)
    else:
        it = iter(args[0])
    most = next(it)
    for key, value in kwargs.items():
        f = value
    for h in it:
        try:
            if f(h) > f(most):
                most = h
        except UnboundLocalError:
            if h > most:
                most = h
    # if len(args) > 1:
    #     it = iter(args)
    # else:
    #     it = iter(args[0])
    # least = next(it)
    # for i in it:
    #     if i > least:
    #         least = i
    #     for key, value in kwargs.items():
    #         if value(i) > value(least):
    #             least = i

    return most


if __name__ == "__main__":
    import doctest
    doctest.testmod()
