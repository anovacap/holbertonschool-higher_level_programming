#!/usr/bin/python3


def number_of_lines(filename=""):
    """
    func number_of_lines - args - filename=""
    """
    line_num = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_num += 1
        return line_num
