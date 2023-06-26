#!/usr/bin/python3

"""function that prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_printed += 1
        except (TypeError, ValueError):
            continue
    print()
    return int_printed
