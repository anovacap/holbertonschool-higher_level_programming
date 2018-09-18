#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    z = len(my_list)
    nl = my_list[:]
    if idx < 0 or idx >= z:
        return my_list
    nl[idx] = element
    return nl
