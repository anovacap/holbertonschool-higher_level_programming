#!/usr/bin/python3
"""
Class Rectangle 14 functions
"""
from models.base import Base
import sys


class Rectangle(Base):
    """
    Class Rectangel - inherits from Class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        func __init__ - args - width, height, x=0, y=0, id=None
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """func width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """func width setter - args - value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """func height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """func height setter - args - value"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """func x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """func x setter - args - value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """func y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """func y setter - args - value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """func - area - no args"""

        return self.__width * self.__height

    def display(self):
        """func display - no args"""

        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """func __str__ - no args"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """func update - args - *args, **kwargs"""

        for i, arg in enumerate(args):
            self.id = args[0]
            if i is 1:
                self.width = args[1]
            elif i is 2:
                self.height = args[2]
            elif i is 3:
                self.x = args[3]
            elif i is 4:
                self.y = args[4]
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """func to_dictionary"""

        d = {}
        d['id'] = self.id
        d['width'] = self.width
        d['height'] = self.height
        d['x'] = self.x
        d['y'] = self.y
        return d
