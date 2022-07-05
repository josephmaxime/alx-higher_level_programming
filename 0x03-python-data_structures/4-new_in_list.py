#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    length = len(my_list)

    if idx < 0 or idx >= length:
        return my_list.copy()

    list_ = my_list.copy()
    list_[idx] = element

    return list_
