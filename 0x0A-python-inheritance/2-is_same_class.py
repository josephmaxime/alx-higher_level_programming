#!/usr/bin/python3
""" 1-is_samee_class module"""


def is_same_class(obj, a_class):
    """function: list of available attributes and methods of an object."""

    test = False

    if isinstance(obj, a_class):
        test = True

    return test
