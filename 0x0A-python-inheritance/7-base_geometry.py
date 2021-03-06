#!/usr/bin/python3
"""
Defines BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Function area - no args
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Func integer_validator - validates value - args - name, value
        """
        name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
