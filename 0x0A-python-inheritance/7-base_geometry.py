#!/usr/bin/python3
""" this module define the class: BaseGeometry"""


class BaseGeometry:
    """ a class BaseGeometry"""
    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ it validates value: you can assume name is always a string"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
