#!/usr/bin/python3


def read_file(filename=""):
    """
    func read_file - args - filename=""
    """
    line_number = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            print('{}'.format(a_line), end="")
