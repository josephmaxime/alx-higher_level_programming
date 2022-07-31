#!/usr/bin/python3
""" Module of matrix multiplication """


def matrix_mul(m_a, m_b):
    """This is function that multiplies 2 matrices."""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if (m_a == []) or (m_a == [[]]):
        raise ValueError("m_a can't be empty")

    size = 0
    for elt in m_a:
        if type(elt) is not list:
            raise TypeError("m_a must be a list of lists")

        for i in elt:
            if (type(i) is not int) and (type(i) is not float):
                raise TypeError("m_a should contain only integers or floats")

        if size == 0:
            size = len(elt)
            size_t = size

        elif size != len(elt):
            raise TypeError("each row of m_a must be of the same size")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if (m_b == []) or (m_b == [[]]):
        raise ValueError("m_b can't be empty")

    for elt in m_b:
        if type(elt) is not list:
            raise TypeError("m_b must be a list")

        for i in elt:
            if (type(i) is not int) and (type(i) is not float):
                raise TypeError("m_b should contain only integers or floats")

        if size == 0:
            size = len(elt)

        elif size != len(elt):
            raise TypeError("each row of m_b must be of the same size")

    if size_t != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_x = mult(m_a, m_b)

    return m_x

def mult(m_a, m_b):
    "This is the function that multiply two matrix"

    res = [[0 for x in range(len(m_b))] for y in range(len(m_a))]

    for i in range(len(m_a)):

        for j in range(len(m_b[0])):

            for k in range(len(m_b[0])):

                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
