#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) is 0:
        return None
    x = "True"
    y = "False"
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(x)
        else:
            new_list.append(y)
    return new_list
