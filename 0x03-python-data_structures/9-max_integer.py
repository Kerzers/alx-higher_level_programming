#!/usr/bin/python3
"""function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if len(my_list) > 0:
        list_sorted = sorted(my_list)
        return(list_sorted[-1])
    return
