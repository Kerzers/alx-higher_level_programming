#!/usr/bin/python3
"""function that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if roman_string is None:
        return
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500, 'M': 1000}
    converted_int = 0
    for char in roman_string:
        converted_int += roman_numeral[char]
    return converted_int
