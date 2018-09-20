#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    d = []
    j = set_1.intersection(set_2)
    h = set_1 | set_2
    for i in h:
        if i in j:
            continue
        d.append(i)
    return d
