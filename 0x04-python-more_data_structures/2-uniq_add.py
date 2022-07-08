#!/usr/bin/python3

def uniq_add(my_list=[]):

    summ = 0

    li = set(my_list)

    for elt in li:

        summ += elt

    return summ
