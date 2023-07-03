#!/usr/bin/python3
""" This module is "0-add_integr"
This module supplies one function, add_integer().  For example,
>>> add_integer(5, 1)
6
"""


def add_integer(a, b=98):
    """ a function that adds 2 integers.
    a and b must be integers or floats, otherwise raise a TypeError
    with message a must be an integer or b must be an integer"""

    if not type(a) == int and not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b) == int and not type(b) == float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
