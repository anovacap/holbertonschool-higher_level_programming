#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    z = 0
    if matrix is None:
        return None
    for i in matrix:
        for x in i:
            if z == i[len(i) - 1]:
                print("{:d}".format(x), end="")
            else:
                print("{:d}".format(x), end=" ")
            z += 1
        print()
