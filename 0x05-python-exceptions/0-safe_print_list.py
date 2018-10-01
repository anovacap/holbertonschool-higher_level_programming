#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for z in range(x):
            print("{}".format(my_list[z]), end="")
            counter += 1
    except:
        pass
    print("")
    return counter
