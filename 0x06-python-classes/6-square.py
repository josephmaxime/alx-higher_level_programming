#!/usr/bin/python3


"""
This Module define a square with #.
"""


class Square:

    """ This Class square define a square. """

    def __init__(self, size=0, position=(0, 0)):

        """Initialize variable of the square class

        Args:

           size (int): The size of a side of the square.
           position (int, int): The position of # in square.

        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size

        if not isinstance(position, tuple):

            if not (isinstance(position[0], int)
                    and isinstance(position[1], int)):

                if (position[0] < 0) and (position[1] < 0):

                    raise TypeError("position must
                                    be a tuple of 2 positive integers")

        self.__position = position

    def area(self):

        """This function returns square of area"""

        return self.__size ** 2

    @property
    def size(self):

        """Retrieve the square size."""

        return self.__size

    @property
    def position(self):

        """Retreive the position of size"""

        return self.__size

    @size.setter
    def size(self, value):

        """Set the new value of a square size

        Args:
           value (int): the new value of the square size.

        """

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):

        """Set the new value of a position

        Args:

           value (int, int): the new value of position.

        """

        if not isinstance(position, tuple):

            if not (isinstance(position[0], int)
                    and isinstance(position[1], int)):

                if (position[0] < 0) and (position[1] < 0):

                    raise TypeError("position must be a
                                    tuple of 2 positive integers")

    def my_print(self):

        """Prints in stdout the square with the character #

        if size is equal to 0, print an empty line.

        position should be use by using space

        """

        ss = self.__size  # ss means square size

        pst = self.__position[0]

        if ss == 0:

            print()

        else:

            for i in range(ss):

                for p in range(pst):

                    print("_", end="")

                for j in range(ss):

                    print("#", end="")

                print()
