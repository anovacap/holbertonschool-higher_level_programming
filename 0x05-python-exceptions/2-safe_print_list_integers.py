#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for z in range(x):
            if type(my_list[z]) is int:
                print("{:d}".format(my_list[z]), end="")
                counter += 1
    except(ValueError, TypeError, SyntaxError):
        pass
    print("")
    return counter
