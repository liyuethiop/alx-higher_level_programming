#!/usr/bin/python3
def print_matrix_integer(matric=[[]]):
    for i in range(len(matric)):
        for j in range(len(matric[i])):
            print("{:d}".format(matric[i][j]), end="")
            if j != (len(matric) - 1):
                print(" ", end="")
        print()
