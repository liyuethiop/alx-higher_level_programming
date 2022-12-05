#!/usr/bin/python3
def print_matrix_integer(matric=[[]]):
    for i in matric:
        for j in i:
            print("{:d} ".format(j), end="")
        print()
