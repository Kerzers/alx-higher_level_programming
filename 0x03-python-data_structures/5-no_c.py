#!/usr/bin/python3
""" function that removes all characters c and C from a string"""


def no_c(my_string):
    new = ''
    for char in my_string:
        if char != "C" and char != "c":
            new = new + char
    return new
