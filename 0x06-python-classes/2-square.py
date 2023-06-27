#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square by: size."""

    def __init__(self, size=0):
        """Initilize a class square by size

        Args:
        size (int): size of square

        Raises:
        ValueError: if size is negativ
        TypeError: if size is not integer

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
