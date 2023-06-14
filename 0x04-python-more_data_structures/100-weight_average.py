#!/usr/bin/python3
""" function that returns the weighted average of
all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mul = 0
    total_weight = 0
    for elmt in my_list:
        mul += elmt[0] * elmt[1]
        total_weight += elmt[1]
    return (mul / total_weight)
