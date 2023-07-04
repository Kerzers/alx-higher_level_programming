#!/usr/bin/python3
""" This is module 4-print_square
This module supplies one function,
that prints a square with the character #.
"""


def print_square(size):
    if size is None or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
