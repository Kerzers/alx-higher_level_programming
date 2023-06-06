#!/usr/bin/python3
def islower(c):
    result = False
    if ord(c) > 90 or ord(c) < 65:
        result = True
    return result
