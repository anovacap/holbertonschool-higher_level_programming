#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sdk = sorted(a_dictionary.keys())
    for k in sdk:
        print("{}: {}".format(k, a_dictionary[k]))
