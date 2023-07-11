#!/usr/bin/python3
""" module defines a function: read_file"""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf_8") as f:
        print(f.read(), end="")
