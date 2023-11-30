#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    argc = len(argv)
    if (argc - 1 == 0):
        message = "arguments."
    elif (argc - 1 == 1):
        message = "argument:"
    else:
        message = "arguments:"
    print("{:d} {}".format(argc - 1, message))
    for i in range(1, argc):
        print("{:d}: {}".format(i, argv[i]))
