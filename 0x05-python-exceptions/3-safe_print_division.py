#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        print("Inside result: {:.1f}".format(c))
        return c
    except(ZeroDivisionError):
        pass
