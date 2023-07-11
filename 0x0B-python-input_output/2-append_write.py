#!/usr/bin/python3
""" module defines function: append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file(UTF8)
    and returns the number of characters written"""

    with open(filename, mode="a", encoding="utf_8") as f:
        return f.write(text)
