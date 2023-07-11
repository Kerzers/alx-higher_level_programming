#!/usr/bin/python3
"""module defines function: load_from_json_file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, mode="r", encoding="utf_8") as f:
        return json.load(f)
