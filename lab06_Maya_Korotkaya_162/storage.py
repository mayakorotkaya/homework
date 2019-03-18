#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy


class Transaction:

    def __init__(self, storage):
        self.storage = storage
        self.copy_storage = deepcopy(storage)

    def __enter__(self):
        return self

    def __exit__(self, type, *args):  # signature is not known
        if type is None:
            self.storage._data = self.copy_storage._data

    def __setitem__(self, key, value):
        self.copy_storage._data[key] = value

    def __getitem__(self, key):
        return self.copy_storage._data[key]

    def __delitem__(self, key):
        del self.copy_storage._data[key]


class Storage:
    """
    >>> try:
    ...     s = Storage()
    ...     with s.edit() as e:
    ...         e['a'] = 1
    ...         1/0
    ...     print(s['a'])
    ... except ZeroDivisionError:
    ...     print(s['a'])
    Traceback (most recent call last):
    ...
    KeyError: 'a'
    """

    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def edit(self):
        return Transaction(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
