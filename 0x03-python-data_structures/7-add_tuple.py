#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero = 0
    la = list(tuple_a)
    lb = list(tuple_b)
    len_a = len(la)
    len_b = len(lb)
    while len_a < 2:
        la.append(zero)
        len_a += 1
    while len_b < 2:
        lb.append(zero)
        len_b += 1
    x = la[0] + lb[0]
    z = la[1] + lb[1]
    return x, z
