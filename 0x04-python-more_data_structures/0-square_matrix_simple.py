#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    len_i = 0
    for elt in matrix:
        len_i += len_i

    len_j = 0
    for num in matrix[0]:
        len_j += len_j

    if len_i == len_j:
        return [[num**2 for num in elt] for elt in matrix]
