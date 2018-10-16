#!/usr/bin/python3
read_file = __import__('0-read_file').read_file
number_of_lines = __import__('1-number_of_lines').number_of_lines
read_lines = __import__('2-read_lines').read_lines


def write_file(filename="", text=""):
    """
    func write_file - args - filename="", text=""
    """
    z = 0
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            for i in a_line:
                z += 1
        return z
