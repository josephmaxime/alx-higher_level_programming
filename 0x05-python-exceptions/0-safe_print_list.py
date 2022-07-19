#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    for elt in range(x):
        try:
            print("{}".format(my_list[elt]), end="")
        except IndexError:
            break
    print()
    return (elt + 1)
