#!/usr/bin/python3
"""
Defines inherits_from
"""


def inherits_from(obj, a_class):
    """
    Function inherits_from - args - obj, a_class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
