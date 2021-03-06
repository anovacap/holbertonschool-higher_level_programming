#!/usr/bin/python3
"""
Defines Class Rectangle
"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """
        __init__ method
        Args: width (int), height (int)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        width
        Args: value (int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        height
        Args: value (int)
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area
        retruns: self.width * self.height
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        perimeter
        returns: (self.width + self.height) * 2
        """
        if self.width is 0 or self.height is 0:
            return 0
        perimeter = (self.width + self.height) * 2
        return perimeter
