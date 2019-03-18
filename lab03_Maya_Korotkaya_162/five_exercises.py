#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source:
# https://docs.python.org/3/library/itertools.html#itertools.filterfalse


def map_(func, iterable):
    """
    The same as built-in map(), but generator
    >>> from collections import Generator
    >>> square = lambda x: x ** 2
    >>> isinstance(map_(square, range(10)), Generator)
    True
    >>> list(map_(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    for i in iterable:
        i = func(i)
        yield i


def zip_(*iterables):
    """
    The same as built-in zip(), but generator
    >>> for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    ...     print(i, j, k)
    0 0 -7
    1 1 -6
    2 2 -5
    """

    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


def dropwhile(predicate, iterable):
    """
    The same as itertools.dropwhile(), but generator
    >>> from collections import Generator
    >>> isinstance(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]), Generator)
    True
    >>> list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    [6, 4, 1]
    """
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x


def filterfalse(predicate, iterable):
    """
    The same as itertools.filterfalse(), but generator
    >>> from collections import Generator
    >>> isinstance(filterfalse(lambda x: x % 2, range(10)), Generator)
    True
    >>> list(filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    """

    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


def unique(iterable, key=None):
    """
    Generates unique values from iterable object
    >>> from collections import Generator
    >>> isinstance(unique(range(10)), Generator)
    True
    >>> list(unique([1, 1, 2, 2, 3, 1, 11, -1]))
    [1, 2, 3, 11, -1]
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


if __name__ == "__main__":
    import doctest
    doctest.testmod()
