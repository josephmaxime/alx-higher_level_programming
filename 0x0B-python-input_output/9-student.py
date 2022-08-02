#!/usr/bin/python3
"""student module.
"""


class Student:
    """class Student."""

    def __init__(self, first_name, last_name, age):
        """ Initialize """

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""

        return self.__dict__
