#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import sqrt


class Vector:
    """
    Class Vector is n-dimensional geometry vector.
    Examples of usage:
    >>> a = Vector([1, 2, 3, 4])
    >>> b = Vector([0, 1, -1, -4])
    >>> a
    Vector([1, 2, 3, 4])
    >>> a + b
    Vector([1, 3, 2, 0])
    >>> a - b
    Vector([1, 1, 4, 8])
    >>> print(a * b)
    Vector([0, 2, -3, -16])
    >>> print(b / a)
    Vector([0.0, 0.5, -0.3333333333333333, -1.0])
    >>> a == Vector([1, 2, 3, 4])
    True
    >>> a.append(144)
    >>> print(a)
    Vector([1, 2, 3, 4, 144])
    >>> len(a)
    5
    >>> a.ndim() == 5
    True
    >>> a[1] == 2
    True
    >>> a[-1] = 5
    >>> a[-1]
    5
    >>> a.clear()
    >>> not a
    True
    >>> b.reverse()
    >>> b
    Vector([-4, -1, 1, 0])
    >>> abs(b) == sqrt(16 + 1 + 1 + 0)
    True
    >>> b.argmin()
    0
    >>> b[b.argmin()] == -4
    True
    >>> b.argmax()
    2
    >>> b[b.argmax()] == 1
    True
    >>> [i for i in b] == [-4, -1, 1, 0]
    True
    """
    def __init__(self, vector):
        self.coords = []
        self.vector = vector
        for i in vector:
            self.coords.append(i)

    def __str__(self):
        return f'Vector({self.coords})'
    __repr__ = __str__

    def __add__(self, other):
        summ = []
        if len(self.coords) == len(other.coords):
            for i in range(0, len(self.coords)):
                summ.append(self.coords[i]+other.coords[i])
            return Vector(summ)
        else:
            raise ValueError

    def __sub__(self, other):
        dif = []
        if len(self.coords) == len(other.coords):
            for i in range(0, len(self.coords)):
                dif.append(self.coords[i]-other.coords[i])
            return Vector(dif)
        else:
            raise ValueError

    def __mul__(self, other):
        mul = []
        if len(self.coords) == len(other.coords):
            for i in range(0, len(self.coords)):
                mul.append(self.coords[i]*other.coords[i])
            return Vector(mul)
        else:
            raise ValueError

    def __truediv__(self, other):
        div = []
        if len(self.coords) == len(other.coords):
            for i in range(0, len(self.coords)):
                div.append(self.coords[i] / other.coords[i])
            return Vector(div)
        else:
            raise ValueError

    def __eq__(self, other):
        coords_bool = self.vector == other.vector
        return coords_bool

    def append(self, new_coord):
        self.append = self.coords.append(new_coord)

    def __len__(self):
        return len(self.coords)

    def ndim(self):
        return len(self.coords)

    def __getitem__(self, key):
        if key <= len(self.coords) - 1:
            return self.coords[key]
        else:
            raise IndexError

    def __setitem__(self, index, coord):
        if index <= len(self.coords) - 1:
            self.coords[index] = coord
        else:
            raise IndexError

    def clear(self):
        self.coords.clear()

    def reverse(self):
        self.coords = self.coords[::-1]

    def __abs__(self):
        summ = 0
        for i in self.coords:
            i = i**2
            summ += i
        return sqrt(summ)

    def argmin(self):
        mass = []
        for i in self.coords:
            i = int(sqrt(abs(i)))
            mass.append(i)
        return min(mass)

    def argmax(self):
        mass = []
        for i in self.coords:
            i = int(sqrt(abs(i)))
            mass.append(i)
        return max(mass)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
