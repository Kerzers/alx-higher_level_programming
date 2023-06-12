#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    for i in range(1, len(my_list) + 1):
        print("{}".format(my_list[-i]))
