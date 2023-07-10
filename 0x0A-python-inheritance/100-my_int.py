#!/usr/bin/python3
""" this module define the class: MyInt"""


class MyInt(int):
    """a class MyInt that inherits from int:
    MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """ changes the behavior of == to !="""
        if super().__eq__(other):
            return False

    def __ne__(self, other):
        """ changes the behavior of != to =="""
        if super().__eq__(other):
            return True
