#!/usr/bin/python3
""" this module defines the class: Base"""


class Base:
    """ this is the class Base defined by:
    attribute:
    nb_objects (int): private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor:
        if id is not None, it assigns the id with its argument value
        otherwise, increment __nb_objects and assign the new value to id
        args:
        id (int): the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
