#!/usr/bin/python3
"""function that returns a new dictionary with all values
multiplied by 2"""


def multiply_by_2(a_dictionary):
    new = {key: a_dictionary[key] * 2 for key in list(a_dictionary)}
    return new
