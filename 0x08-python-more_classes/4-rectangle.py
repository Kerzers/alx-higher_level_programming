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

    def area(self):
        """that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """rints a rectangle instance with the same behavior as my_print()"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            result += "#" * self.__width + '\n'
        result = result.rstrip('\n')
        return result

    def __repr__(self):
        """ return astring representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        result = "Rectangle(" + str(self.__width) + ", " \
                 + str(self.__height) + ")"
        return result
