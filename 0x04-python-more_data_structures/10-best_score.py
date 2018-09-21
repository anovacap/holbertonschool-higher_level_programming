#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        j = max(a_dictionary.values())
        if j in a_dictionary.values():
            p = {k for k, v in a_dictionary.items() if v == j}
            s = p.pop()
            return s
