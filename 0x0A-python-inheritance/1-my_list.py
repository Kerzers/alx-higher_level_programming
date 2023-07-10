#!/usr/bin/python3
""" module that defines subclass MyList"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
