#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import sys
import traceback


@contextmanager
def supresser(*types_):
    """
    Context manager supresses all exceptions with specified types
    >>> with supresser(ZeroDivisionError):
    ...     print("OK")
    ...     1/0
    ...
    OK
    """
    try:
        yield
    except types_:
        pass


@contextmanager
def retyper(type_from, type_to):
    """
    Context manager changes type of exception to another type, saves
    all attributes (args and __traceback__). And raises new exception again
    >>> try:
    ...     with retyper(ValueError, TypeError):
    ...         raise ValueError("wrong cast")
    ... except TypeError as e:
    ...     print(e.args[0])
    ...
    wrong cast
    """
    raise NotImplementedError


def dumper(stream=None):
    """
    Context manager dumps an exception to stream
    (dumps value and traceback of exception). Stream object must implement
    write() method. Then raises exception again
    >>> with open("dump.txt", 'w') as s, dumper(stream=s):
    ...     raise LookupError("lookup error")
    ...
    Traceback (most recent call last):
    ...
    LookupError: lookup error
    """
    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
