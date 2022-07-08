#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    if my_list:
        new_list = my_list.copy()

        return [elt * number for elt in new_list]
