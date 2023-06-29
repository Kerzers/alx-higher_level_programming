#!/usr/bin/paython3
""" This module defines Class Square"""


class Square:
    """ This is class square defined by attributes: size and position
    Attributes:
        size (int): size of a square
        position (int, int): coordinates if a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the object square
        Args:
        size (int): size of a square
        position (int, int): coordinates if a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Set/retreive the value of size to/from an object Square"""
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
        """Set/retreive the value of position to/from an object Square"""

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        try:
            for i in range(2):
                if not isinstance(value[i], int) or value[i] < 0:
                    raise Exception
            self.__position = value
        except Exception:
            print("position must be a tuple of 2 positive integer")

    def area(self):
        """Public instance method: calculates the area of a square.

        Returns:
        the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #
        if size = 0, prints empty line
        """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()
            return

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Prints a Square instance with the same behavior as my_print()"""
        result = ""
        if self.__size == 0:
            return result
        result += '\n' * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size + '\n'
        result = result.rstrip('\n')
        return result
