#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:

        max_ = max(list(a_dictionary.values()))

        for key, value in a_dictionary.items():
            if value == max_:
                return key

    return None
