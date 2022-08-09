#!/usr/bin/python3
""" Module models base """


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor """

        if id is not None:
            self.id = id

        else:
             __nb_objects += 1 
            id = self.id
