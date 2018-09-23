#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    mult_tup = [x * y for x, y in my_list]
    sum_tup = sum(mult_tup)
    ylst = [y for x, y in my_list]
    sum_ylist = sum(ylst)
    res = sum_tup / sum_ylist
    return res
