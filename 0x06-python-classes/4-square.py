#!/usr/bin/python3

class Square:
    '''a class Square that defines a square by'''

    def __init__(self, size=0):
        '''Private instance attribute'''
        self.__size = size

    @property
    def size(self):
        '''property getter to retrieve size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter to set size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Public instance method that returns the current square area'''
        return (pow(self.__size, 2))
