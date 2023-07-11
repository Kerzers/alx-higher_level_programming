#!/usr/bin/python3
""" module that defines class: Student"""


class Student:
    """a class Student that defines a student by:
    Public instance attributes:
    first_name (str)
    last_name (str)
    age (int)
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """ Initialization of an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved"""

        if attrs is None:
            return vars(self)
        a_dict = {}
        for attribute in attrs:
            if hasattr(self, attribute):
                a_dict[attribute] = getattr(self, attribute)
        return a_dict
