#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from typing import List
from numbers import Number


def regexp_0(text: str, pattern: str) -> List[slice]:
    """
    Finds the occurrence and position of the substrings within a string
    >>> regexp_0("LingvoX SpaceX SpacoX", "oX")
    [slice(5, 7, None), slice(19, 21, None)]
    """
    mass = []
    for i in range(len(text)):
        res = re.match(pattern, text[i:])
        if res is not None:
            mass.append(slice(i, res.end() + i))
    return mass


def regexp_1(text: str) -> str:
    """
    Converts camel case string to snake case string
    >>> regexp_1("QObject")
    'q_object'
    >>> regexp_1("KNeighborsClassifier")
    'k_neighbors_classifier'
    """
    pattern = r'[a-z, A-Z][A-Z]'
    for i in range(len(text)):
        res = re.match(pattern, text[i:])
        if res is not None:
            text = re.sub(res.group(0),
                          text[i].lower() + '_' + text[i + 1].lower(), text)
    return text


def regexp_2(text: str, length: int) -> str:
    """
    Removes words from a string of length between 1 and a given number
    >>> regexp_2("Hello Cyril Kak dela bro", 3)
    'Hello Cyril dela'
    >>> regexp_2("Hello Cyril Kak dela bro", 4)
    'Hello Cyril'
    """
    text = re.split(' ', text)
    text1 = []
    for i in text:
        if len(i) > length:
            try:
                text1.append(i)
            except ValueError:
                pass
    line = ' '.join(text1)
    return line


def regexp_3(text: str) -> str:
    """
    Removes the parenthesis area in a string
    >>> regexp_3("Polina (Ivan)")
    'Polina'
    >>> regexp_3("Mark (Station) (LingvoX)")
    'Mark'
    """
    res = re.sub(r' \(.*?\)', '', text)
    return res


def regexp_4(num: Number) -> bool:
    """
    Returns true whenever a decimal with a precision of 2
    >>> regexp_4(1.22)
    True
    >>> regexp_4(1.2)
    True
    >>> regexp_4(11)
    True
    >>> regexp_4(11.)
    True
    >>> regexp_4(11.333)
    False
    """
    # res = num * 100
    # res = str(res)
    # return res[-1] == '0'

    res = re.search('\.\d{,2}$', str(float(num)))
    return res is not None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
