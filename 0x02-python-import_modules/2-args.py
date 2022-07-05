#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    arg = "argument"
    length = len(argv)
    print("{} {}{}".format(length - 1, arg if length == 2
                           else arg+"s", "." if length == 1 else ":"))

    for args in range(length):
        if args > 0:
            print("{}: {}".format(args, argv[args]))
