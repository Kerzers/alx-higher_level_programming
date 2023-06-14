#!/usr/bin/python3
"""function that deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):
    keys = []
    for key, val in a_dictionary.items():
        if val == value:
            keys.append(key)
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
