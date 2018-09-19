#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if len(sentence) is 0:
        return x, None
    else:
        j = sentence[0]
        return x, j
