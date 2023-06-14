#!/usr/bin/python3
"""function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
