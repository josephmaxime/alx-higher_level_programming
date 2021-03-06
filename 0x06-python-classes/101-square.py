#!/usr/bin/python3


"""This Module define a square
where the size is represented by # and
the position of square by value of position."""


class Square:
    """This Class square define a square."""

    def __init__(self, size=0, position=(0, 0)):

        """Initialize variable of the square class

        Args:
           size (int): The size of a side of square.
                initialize by 0.
           position (int, int): The position of square.
                initialize by (0, 0).

        """

        err_position = "position must be a tuple of 2 positive integers"

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size

        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and
                position[1] >= 0):

            raise TypeError(err_position)

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

        return self.__position

    @size.setter
    def size(self, value):

        """Set the new value of a square size

        Args:
           value (int): the new value of the square size
                 value >= 0.

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

        err_position = "position must be a tuple of 2 positive integers"

        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and
                position[1] >= 0):

            raise TypeError(err_position)

        self.__position = value

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

            for i in range(self.__position[1]):

                print()

            for i in range(ss):

                for p in range(pst):

                    print(end=" ")

                for j in range(ss):

                    print("#", end="")

                print()

    def __str__(self):
        """ Print square in stdout."""

        ch = ""
        ss = self.__size  # ss means square size
        pst = self.__position[0]

        if ss == 0:

            ch += ""

        else:

            for i in range(self.__position[1]):

                ch += "\n"

            for i in range(ss):

                for p in range(pst):

                    ch += " "

                for j in range(ss):

                    ch += "#"

                if i < ss - 1:

                    ch += "\n"

        return ch
