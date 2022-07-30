#!/usr/bin/python3
"""Module add integer"""


def add_integer(a, b=98):
    """Function to add two integer for testing

    Args:
        a (int or float): integer or float.
        b (int or float): integer or float initialize at 98.
    """

    if (type(a) in [int, float]):

        if (type(a) is float):

            a = int(a)
    else:
        raise TypeError("a must be an integer")

    if (type(b) in [int, float]):

        if (type(b) is float):

            b = int(b)
    else:
        raise TypeError("b must be an integer")

    return (a + b)
