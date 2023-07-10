#!/usr/bin/python3
""" this module define the class: Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry
    Attributes:
    width (int): width of rectangle
    height(int): height of a rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """ prints the information about a rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
