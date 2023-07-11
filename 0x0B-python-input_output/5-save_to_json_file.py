#!/usr/bin/python3
"""module defines function: save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""

    with open(filename, mode="w", encoding="utf_8") as f:
        json.dump(my_obj, f)
