#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    num = 0
    for i in range(1, len(argv)):
        num += int(argv[i])
    print("{:d}".format(num))
