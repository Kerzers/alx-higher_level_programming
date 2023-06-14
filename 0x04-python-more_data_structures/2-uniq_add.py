#!/usr/bin/python3
""" function that adds all unique integers in a list
(only once for each integer)"""


def uniq_add(my_list=[]):
    sum = 0
    uniq = set(my_list)
    for x in uniq:
        sum += x
    return sum
