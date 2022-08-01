#!/usr/bin/python3

"""add_attribute module"""


def add_attribute(obj, attr_name, attr_value):

    """Adds a new attribute to an object if it is possible"""

    if '__dict__' not in dir(obj):

        raise TypeError('can\'t add new attribute')

    else:

        obj.__dict__[attr_name] = attr_value
