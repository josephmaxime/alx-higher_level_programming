#!/usr/bin/python3

"""
That is "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""

    if type(matrix) is not list:

        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None

    for list_ in matrix:

        if type(list_) is not list:

            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if size is None:
            size = len(list_)

        elif size != len(list_):
            raise TypeError("Each row of the matrix must have the same size")

        for elt in list_:

            if type(elt) is not int and type(elt) is not float:

                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in elt] for elt in matrix]
