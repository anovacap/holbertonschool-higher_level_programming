#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    func append_write - args - filename, text
    """
    z = 0
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            for i in a_line:
                z += 1
    return z
