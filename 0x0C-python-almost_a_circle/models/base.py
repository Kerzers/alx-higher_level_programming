#!/usr/bin/python3
""" this module defines the class: Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """it returns the JSON string representation of list_dictionaries:
        Args:
        list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ it writes the JSON string representation of list_objs to a file
        Args:
        list_objs (list): list of instances who inherits of Base
        cls (type): the class
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                str_json = Base.to_json_string(list_dict)
                f.write(str_json)

    @staticmethod
    def from_json_string(json_string):
        """ it returns the list of the JSON string representation
        Args:
        json_string (str): the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set:
        args:
            dictionary (dict): key/value pair to intialize an instance
        """
        new = cls(1, 1)
        new.update(**dictionary)
        return new
