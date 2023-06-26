#!/usr/bin/python3

"""function prints integer"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
