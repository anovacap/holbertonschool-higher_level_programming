#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    l = len(my_list)
    if l == 0:
        return None
    if idx < 0 or idx >= l:
        return my_list
    else:
        del my_list[idx]
        return my_list
