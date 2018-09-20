#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        j = max(a_dictionary.keys())
        return j
    else:
        return None
