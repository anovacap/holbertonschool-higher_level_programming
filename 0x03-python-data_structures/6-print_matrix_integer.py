#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for i in matrix:
        for x in i:
            if x == i[len(i) - 1]:
                print("{:d}".format(x), end="")
            else:
                print("{:d}".format(x), end=" ")
        print()
