#!/usr/bin/python3
class Square:
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        sq_area = self.__size ** 2
        return sq_area

    def my_print(self):
        a, b = self.__position
        for i in range(b):
            print("")
        for i in range(self.__size):
            print("{}{}".format(a * " ", self.__size * "#"),  end="")
            print("")
        if self.__size is 0:
            print("")
