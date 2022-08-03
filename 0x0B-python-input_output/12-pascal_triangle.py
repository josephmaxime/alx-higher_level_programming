#!/usr/bin/python3
"""Pascal's triangle module"""


def pascal_triangle(n):
    """Function  that returns a list of lists of integers
    representing the Pascal's triangle of n


    if (n <= 0):
        return [[]]

    else:
        list_pascal = [[1]]

        for i in range(n - 1):

            tmp = [1]
            list_t = list_pascal[-1]
            for j in range(len(list_t)):

                try:
                    tmp.append(list_[j] + list_[j + 1])
                except Exception:
                    pass

            tmp.append(1)
            list_pascal.append(tmp)

        return list_pascal
    """

    if n <= 0:
        return []

    else:

        list_pascal = [[1]]

        for i in range(n - 1):

            tmp = [1]

            last_element = list_pascal[-1]

            for j in range(len(last_element)):

                try:

                    tmp.append(last_element[j] + last_element[j + 1])

                except Exception:

                    pass

            tmp.append(1)

            list_pascal.append(tmp)

        return list_pascal
