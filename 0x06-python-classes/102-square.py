#!/usr/bin/python3


"""4-square Module"""


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

    @property
    def size(self):

        """Retrieve the square size."""

        return self.__size

    @size.setter
    def size(self, value):

        """Set the new value of a square

        Args:

            value (int): the new value of the square size.

        """

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, value):

        """Returns True if the area of square self = area of value.

            otherwise False.

        """

        return self.area() == value.area()

    def __ne__(self, value):

        """Returns True if the area of square self != area of value.

            otherwise False.

        """

        return not self.__eq__(value)

    def __gt__(self, value):

        """Returns True if the area of square self > area of value.

            otherwise False.

        """

        return self.area() > value.area()

    def __ge__(self, value):

        """Returns True if the area of square self >= area of value.

            otherwise False.

        """

        return self.area() >= value.area()

    def __lt__(self, value):

        """Returns True if the area of square self < area of value.

            otherwise False.

        """

        return not self.__ge__(value)

    def __le__(self, value):

        """Returns True if the area of square self <= area of value.

            otherwise False.

        """

        return not self.__gt__(value)
