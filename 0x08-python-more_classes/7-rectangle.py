#!/usr/bin/python3
"""
Defines Class Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        __init__ method
        Args: width (int), height (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        __str__
        returns: printed rectangle
        """
        if self.width is 0 or self.height is 0:
            return ""
        if self.height is 1:
            return str(self.print_symbol) * self.width
        s = ""
        for i in range(self.height - 1):
            s += str(self.print_symbol) * self.width + "\n"
            if i is self.height - 2:
                s += str(self.print_symbol) * self.width
        return s

    def __repr__(self):
        """
        __repr__ method
        returns: Rectangle(width, heaight)
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        __del__ method
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
