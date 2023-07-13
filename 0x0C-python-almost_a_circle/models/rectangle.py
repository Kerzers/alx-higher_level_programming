#!/usr/bin/python3
""" module rectangle defines class: Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ It initializes the object from class Rectangle
        args:
        width (int): the width of a rectangle (Private instance attribute)
        height (int): the height of a rectangle (Private instance attribute)
        x (int): the abscissa
        y (int): the ordinate
        id (int): the id of the object
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get/Set the value of/from width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve/set the value of/from height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Get/Set the value of/from x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Get/Set the value of/from y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
