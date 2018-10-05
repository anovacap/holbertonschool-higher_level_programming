#!/usr/bin/python3
"""
Defines funtion print_square(size) where size is the size length of the square
"""


def print_square(size):
    """
    Prints a square of size dimensions
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("{}".format("#" * size))
