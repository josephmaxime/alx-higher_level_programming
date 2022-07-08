#!/usr/bin/python3

def uniq_add(my_list=[]):

    summ = 0

    l = set(my_list)

    for elt in l:

        summ += elt

    return summ
