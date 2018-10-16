#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    func load_from_json_file - args - filename
    """
    with open(filename) as a_file:
        return json.load(a_file)
