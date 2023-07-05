#!/usr/bin/python3
"""Module defines a class LockedClass"""


class LockedClass:
    """ LockedClass with no class or object attribute,
    it prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ("first_name",)
