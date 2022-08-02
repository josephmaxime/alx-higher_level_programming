#!/usr/bin/python3
"""student module.
"""


class Student:
    """class Student."""

    def __init__(self, first_name, last_name, age):
        """ Initialize """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of
        a Student instance in attrs list.
        """
        if attrs is None:
            return self.__dict__

        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """function that replaces all attributes of the Student instance"""

        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
