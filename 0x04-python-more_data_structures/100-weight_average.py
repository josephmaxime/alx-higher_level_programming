#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list == []:
        return 0

    num = 0
    den = 0
    for elt in my_list:
        for i in range(len(elt) - 1):
            num += elt[i] * elt[i + 1]
            den += elt[i + 1]

    return num / den
