#!/usr/bin/python3


"""3-square Module"""


class Square:
    """ Class square define a square """

    def __init__(self, size=0):

        """Initialize variable of the square class

        Args:

           size (int): The size of a side of the square.

        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """This function returns square of area"""

        return self.__size ** 2
