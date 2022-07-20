#!/usr/bin/python3


"""2-square Module"""


class Square:
    """ Class square define a square """

    def __init__(self, size=0):

        """Initialize variable of the square class

        Args:

           size (int): The size of a side of the square.

        """

        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
