#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    num = min(my_list)
    for i in my_list:
        if i > num:
            num = i
    return num
