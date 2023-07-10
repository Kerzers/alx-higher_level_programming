#!/usr/bin/python3
""" module that defines a function: inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
    obj: the object
    a_class: a class
    """
    if (isinstance(obj, a_class)) and type(obj) != a_class:
        return True
    return False
