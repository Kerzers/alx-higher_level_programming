#!/usr/bin/python3
""" module that defines a function: is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is exactly an
    instance of the specified class, or if the object is an instance of
    a class that inherited from, otherwise False.
    Args:
    obj: the object
    a_class: a class
    """
    return (isinstance(obj, a_class))
