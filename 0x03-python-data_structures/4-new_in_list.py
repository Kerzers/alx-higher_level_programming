#!/usr/bin/python3
"""function that replaces an element of a list at a specific position
without modifing the original"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    cpy_list = my_list.copy()
    cpy_list.pop(idx)
    cpy_list.insert(idx, element)
    return (cpy_list)
