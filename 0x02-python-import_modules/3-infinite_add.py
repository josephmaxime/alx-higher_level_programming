#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    arg = "argument"
    length = len(argv)
    summ = 0

    for args in range(length):
        if args > 0:
            summ += int(argv[args])

    print("{}".format(summ))
