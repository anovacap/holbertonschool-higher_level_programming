#!/usr/bin/python3


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        func __init__ args - first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        func to_json no args
        """
        dicti = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i is "first_name":
                dicti[i] = self.first_name
            elif i is "last_name":
                dicti[i] = self.last_name
            elif i is "age":
                dicti[i] = self.age
        return dicti

    def reload_from_json(self, json):
        """
        func reload_from_json -args- json
        """
        self.__dict__ = json
