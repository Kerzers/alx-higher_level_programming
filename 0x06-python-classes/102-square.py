#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square by: size."""

    def __init__(self, size=0):
        """Initilize a class square by size

        Args:
        size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method: calculates the area of a square.

        Returns:
        the current square area
        """
        return self.__size * self.__size

    def __lt__(self, other):
        """ Defines the behavior for the less than (<) operator"""
        return self.size < other.size

    def __gt__(self, other):
        """ Defines the behavior for the greater than (>) operator"""
        return self.size > other.size

    def __le__(self, other):
        """ Defines the behavior for the less than or equal (<=) operator"""
        return self.size <= other.size

    def __ge__(self, other):
        """ Defines the behavior for the greater than or equal (>=) operator"""
        return self.size >= other.size

    def __eq__(self, other):
        """ Defines the behavior for the equality (==) operator"""
        return self.size == other.size

    def __ne__(self, other):
        """ Defines the behavior for the not equal (!=) operator"""
        return self.size != other.size
