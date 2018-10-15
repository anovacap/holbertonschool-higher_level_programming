#!/usr/bin/python3
"""
Defines lookup(obj) returns a list of avail attributes and methods
"""


def lookup(obj):
    """
    returns a list of avail attributes and methods
    """
    return dir(obj)
