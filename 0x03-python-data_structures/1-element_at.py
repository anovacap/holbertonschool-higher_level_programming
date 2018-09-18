#!/usr/bin/python3
def element_at(my_list, idx):
    z = len(my_list)
    if idx < 0 or idx > z:
        return None
    if idx <= z:
        return my_list[idx]
