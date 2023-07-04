#!/usr/bin/python3
"""This is module 5-text_indentation.
This module supplies one function, text_indentation
"""


def text_indentation(text):
    """ that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for c in text:
        result += c
        if c in ".:?":
            result += "\n\n"
    result = result.rstrip('\n')
    print(result)
