#!/usr/bin/python3
"""
Defines function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides an even matrix by an integer
    """
    m = []
    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if div is float('inf') or div is float('nan'):
        raise TypeError("div must be a number")
    it = iter(matrix)
    len_mat = len(next(it))
    if not all(len(k) == len_mat for k in it):
        raise TypeError("Each row of the matrix must have the same size")
    if matrix == [] or matrix == [[]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(div, int):
            i = list(map(lambda i: round(i / div, 2), x))
        elif isinstance(div, float):
            i = list(map(lambda i: round(i / div, 2), x))
        else:
            raise TypeError("div must be a number")
        m.append(i)
    return m
