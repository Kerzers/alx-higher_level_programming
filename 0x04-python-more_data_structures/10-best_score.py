#!/usr/bin/python3
"""function that returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return
    score = []
    for key in a_dictionary:
        score.append(a_dictionary[key])
        score.sort()
    for key, value in a_dictionary.items():
        if value == score[-1]:
            return key
