#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

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
        for i in range(self.__size):
            for z in range(self.__size):
                print('#', end="")
            print("")
        if self.__size is 0:
            print("")
