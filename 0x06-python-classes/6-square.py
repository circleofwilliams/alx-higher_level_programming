#!/usr/bin/python3

class Square:
    '''a class Square that defines a square by'''

    def __init__(self, size=0, position=(0, 0)):
        '''Private instance attribute'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''property getter to retrieve position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''property setter to set position'''
        if not isinstance(value, tuple) and (position[:] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Method that returns the current square area'''
        return (pow(self.__size, 2))

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
