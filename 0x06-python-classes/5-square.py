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
        return (int(self.__size) * int(self.__size))

    def my_print(self):
        """ prints in stdout the square with the character #
        if size = 0, prints empty line
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
