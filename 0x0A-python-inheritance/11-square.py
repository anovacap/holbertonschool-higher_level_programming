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


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        """
        func - __init__ - args - width, height
        """
        self.__width = width
        self.__height = height
        self.integer_validator(self.__width, self.__height)

    def area(self):
        """
        func area - no arguments
        """
        return self.__width * self.__height

    def __str__(self):
        """
        func str - no args
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    Class Square - Type - Rectangle
    """
    def __init__(self, size):
        """
        func - __init__ - args - size
        """
        self.__size = size

    def integer_validator(self, size):
        """
        Func integer_validator - validates value - args - __size
        """
        if type(self.__size) is not int:
            raise TypeError("{} must be an integer".format(self.__size))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.__size))

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """
        Func - __str__ - no args
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
