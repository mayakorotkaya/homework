#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def factorial(n):
    """
    Return factorial of integer n.
    Raises ValueError if n is not exact integer or is negative.
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> [factorial(i) for i in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial('121')
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer!
    >>> factorial([1])
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer!
    >>> factorial(1.12)
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer!
    >>> factorial(-10)
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be nonnegative!
    >>> import math
    >>> n = 1000
    >>> math.factorial(n) == factorial(n)
    True
    >>> import random
    >>> n = random.randint(1500, 2000)
    >>> math.factorial(n) == factorial(n)
    True
    """

    if not isinstance(n, int):
        raise ValueError("Argument n must be integer!")

    if not n >= 0:
        raise ValueError("Argument n must be nonnegative!")

    result = 1

    for value in range(1, n+1):
        result = result * value

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
