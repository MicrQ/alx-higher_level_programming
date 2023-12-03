#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in matrix:
        for j in range(0, len(i)):
            if j < len(i) - 1:
                endChar = " "
            else:
                endChar = ""
            print("{:d}".format(i[j]), end=endChar)
        print()
