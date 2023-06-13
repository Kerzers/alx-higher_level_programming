#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        for i in range(1, len(my_list) + 1):
            print("{:d}".format(my_list[-i]))
