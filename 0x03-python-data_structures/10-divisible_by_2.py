#!/usr/bin/python3
"""function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    divisible = [True if elmt % 2 == 0 else False for elmt in my_list]
    return divisible
