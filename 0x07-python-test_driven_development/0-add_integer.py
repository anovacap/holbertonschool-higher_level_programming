#!/usr/bin/python3
"""
Defines a function that adds 2 integers together
"""


def add_integer(a, b=98):
    """
    Adds 2 intgers or floats together
    """

    if a is float('inf') or a is float('nan'):
        raise TypeError("a must be an integer")
    if b is float('inf') or b is float('nan'):
        raise TypeError("b must be an integer")
    if type(a) is  int or type(a) is  float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is  int or type(b) is  float:
        b =int(b)
    else:
        raise TypeError("b must be an integer")
    c = a + b
    return c
