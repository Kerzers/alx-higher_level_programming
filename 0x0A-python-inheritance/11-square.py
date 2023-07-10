#!/usr/bin/python3
""" this module define the class: square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class square that inherits Rectangle class
    Attributes:
    size(int): size of a square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of a square"""
        return (super().area())

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
