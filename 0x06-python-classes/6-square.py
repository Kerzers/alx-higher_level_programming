#!/usr/bin/python3
"""module defines a square"""


class Square:
    """Class Square that defines a square by: size, position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initilize a class square by size and position

        Args:
        size (int): size of square
        position (int, int):tuple that gives the coordinates of a square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(2):
            if not isinstance(value[i], int) or value[i] < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = value

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
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
