#!/usr/bin/python3

""" function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        len_list = 0
        for item in my_list:
            len_list += 1
        print()
        return len_list
