#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date


class Person:
    """
    >>> p = Person('Ivan', 'Ivanov', 'male', date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 29 years
    >>> p.full_ages()
    29
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(self, name, surname, sex, bday):
        self.name = name
        self.surname = surname
        self.sex = sex
        if type(bday) == date:
            self.bday = bday
        else:
            raise ValueError('bday must be date type')

    def full_ages(self):
        now = date.today()
        age = 0
        if self.bday.month < now.month:
            age = now.year - self.bday.year
        if self.bday.month == now.month:
            if self.bday.day < now.day:
                age = now.year - self.bday.year
            else:
                age = now.year - self.bday.year - 1
        if self.bday.month > now.month:
            age = now.year - self.bday.year - 1
        return age

    def __str__(self):
        return f'{self.name} {self.surname},' \
               f' {self.sex}, {self.full_ages()} years'


class Student:
    """
    >>> s = Student('Ivan', 'Ivanov', 'male', date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 29 years, 161 group, 9 skill
    """
    def __init__(self, name, surname, sex, bday, group, skill):
        self.name = name
        self.surname = surname
        self.sex = sex
        if type(bday) == date:
            self.bday = bday
        else:
            raise ValueError('bday must be date type')
        self.group = group
        self.skill = skill

    def full_ages(self):
        now = date.today()
        age = 0
        if self.bday.month < now.month:
            age = now.year - self.bday.year
        if self.bday.month == now.month:
            if self.bday.day < now.day:
                age = now.year - self.bday.year
            else:
                age = now.year - self.bday.year - 1
        if self.bday.month > now.month:
            age = now.year - self.bday.year - 1
        return age

    def __str__(self):
        return f'{self.name} {self.surname}, {self.sex},' \
               f' {self.full_ages()} years,' \
               f' {self.group} group, {self.skill} skill'


class Group:
    """
    Encapsulates list of students
    """
    
    def sort_by_age(self, reverse=False):
        raise NotImplementedError

    def sort_by_skill(self, reverse=False):
        raise NotImplementedError

    def sort_by_age_and_skill(self, reverse=False):
        raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
