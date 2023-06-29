#!/usr/bin/python3
""" Module defines magic class"""
import math


class MagicClass:
    """ Class MgicClass defined by an attribute:
    raduis: radius of a circle
    """
    def __init__(self, radius=0):
        """Initilize the object of MagicClass"""
        if not type(radius) == int and not type(radius) == float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """ Calculates the area of a circle"""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Calculates circumference of a cercle"""
        return 2 * math.pi * self.raduis
