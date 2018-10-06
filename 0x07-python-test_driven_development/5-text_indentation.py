#!/usr/bin/python3
"""
Defines function text_indentation(text), where text must be type str
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    l = []
    for i in text:
        l += i
        if i in ".:?":
            l += "\n\n"
    q = "".join(l)
    d = q.splitlines()
    i = 0
    for w in d:
        i += 1
        s = w.strip()
        if i < len(d):
            print(s)
        else:
            print(s, end="")
