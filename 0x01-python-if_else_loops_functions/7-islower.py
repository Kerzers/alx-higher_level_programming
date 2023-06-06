#!/usr/bin/python3
def islower(c):
    result = False
    if ord(c) > 96 and ord(c) < 123:
        result = True
    return result
