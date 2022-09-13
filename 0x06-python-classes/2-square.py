#!/usr/bin/python3


class Square:
    '''a class Square that defines a square by'''

    def __init__(self, size=0):
        '''Private instance attribute'''
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
