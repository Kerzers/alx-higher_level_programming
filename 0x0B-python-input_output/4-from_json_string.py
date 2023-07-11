#!/usr/bin/python3
"""module defines function: from_json_string"""
import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string"""
    return json.JSONDecoder().decode(my_str)
