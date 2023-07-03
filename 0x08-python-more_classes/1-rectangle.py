#!/usr/bin/python3
"""module defines a rectangle"""


class Rectangle:
    """Class Rectangle that defines a rectangle by: width, height."""

    def __init__(self, width=0, height=0):
        """Initilize a class Rectangle

        Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the value of width"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve the value of position"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
