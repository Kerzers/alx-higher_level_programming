#!/usr/bin/python3
"""module defines a function: add_attribute"""


def add_attribute(obj, attribute, value):
    """ function that adds a new attribute to an object if it’s possible"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
