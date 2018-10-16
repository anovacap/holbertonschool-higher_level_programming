#!/usr/bin/python3
number_of_lines = __import__('1-number_of_lines').number_of_lines
read_file = __import__('0-read_file').read_file


def read_lines(filename="", nb_lines=0):
    """
    func read_lines - args - filename, nb_lines
    """
    if nb_lines <= 0 or nb_lines >= number_of_lines(filename):
        read_file(filename)
    else:
        with open(filename, encoding='utf-8') as a_file:
            for i, a_line in enumerate(a_file):
                if i < nb_lines:
                    print("{}".format(a_line.rstrip(), end=""))
