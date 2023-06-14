#!/usr/bin/python3
"""function that replaces all occurrences of an element
by another in a new list"""


def search_replace(my_list, search, replace):
    new = []
    for x in my_list:
        if x == search:
            new.append(replace)
        else:
            new.append(x)
    return new
