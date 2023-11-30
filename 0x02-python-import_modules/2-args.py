#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys as s
    argc = len(s.argv)
    print("{:d} arguments".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {}".format(i, s.argv[i]))
