#!/usr/bin/python3
""" module that defines a function: is_same_class"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    Args:
    obj: the object
    a_class: a class
    """
    if type(obj) != a_class:
        return False
    return True
