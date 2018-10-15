#!/usr/bin/python3
"""
Defines class MyList - method print_sorted
"""


class MyList(list):
    """
    Class Mylist base class list
    """
    def __init__(self):
        """init method"""
        pass

    def print_sorted(self):
        """Method print_sorted - sorts and prints"""
        l = list.copy(self)
        list.sort(l)
        print(l)
