#!/usr/bin/python3
""" this module defines the class: Base"""
import json
import csv


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
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ it returns a list of instances:
        The filename must be: <Class name>.json - example: Rectangle.json
        If the file doesn’t exist, return an empty list
        Otherwise, return a list of instances:
        the type of these instances depends on cls
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                str_j = f.read()
        except FileNotFoundError:
            return []

        list_output = cls.from_json_string(str_j)
        list_of_instance = list()
        for elmt in list_output:
            list_of_instance.append(cls.create(**elmt))
        return list_of_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV
        Args:
        list_objs (list): list of objects to serialize
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            if list_objs is None or len(list_objs) == 0:
                csv.write(f).writerow("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fieldnames)
                list_of_instance = list()
                for row in reader:
                    row_dict = dict([(k, int(v)) for k, v in row.items()])
                    list_of_instance.append(cls.create(**row_dict))
            return list_of_instance
        except FileNotFoundError:
            return []
