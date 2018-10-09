#!/usr/bin/python3
"""
Defines Class Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """
    function __init__ initializes class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    """
    Defines function width to retrieve __width
    """
    @property
    def width(self):
        return self.__width
    """
    funtction width setter
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """
    function height getter
    """
    @property
    def height(self):
        return self.__height
    """
    function height setter
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """
    function area returns rectangle area
    """
    def area(self):
        area = self.width * self.height
        return area
    """
    function perimeter returns rectangle perimeter
    """
    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        perimeter = (self.width + self.height) * 2
        return perimeter
    """
    function __str__ returns printed area with #
    """
    def __str__(self):
        s = ""
        for i in range(self.height):
            s += str(self.print_symbol) * self.width + "\n"
            if i is self.height - 1:
                s += str(self.print_symbol) * self.width
        return s
    """
    function __repr__ returns a string representation of the rectangle
    """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    """
    function __del__ deletes an instance of rectangle
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    """
    function bigger_or_equal takes rect_1, rect_2 returns biggest rectangle
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
    """
    function square returns a new Rectangle
    """
    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
