#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) == 1:
        list_a = [list_a[0], 0]
    elif len(list_a) == 0:
        list_a = [0, 0]
    else:
        list_a[2:] = []

    if len(list_b) == 1:
        list_b = [list_b[0], 0]
    elif len(list_b) == 0:
        list_b = [0, 0]
    else:
        list_b[2:] = []

    list_a[0] = list_a[0] + list_b[0]
    list_a[1] = list_a[1] + list_b[1]

    tupl = tuple(list_a)

    return tupl
