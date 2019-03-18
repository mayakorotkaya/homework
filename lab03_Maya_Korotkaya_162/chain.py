#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from collections import Iterable


def chain(*args):
    """
    >>> list(chain([[["test"]]]))
    ['t', 'e', 's', 't']
    """
    mass = []

    def chain_nested(lst):
        for x in lst:
            if isinstance(x, Iterable) and not isinstance(x, str):
                yield from chain_nested(x)
            else:
                yield x

    for h in chain_nested(args):
        if type(h) == int:
            mass.append(h)
        else:
            mass.extend(h)
    yield from mass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
