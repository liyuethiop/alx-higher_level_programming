#!/usr/bin/python3
def max_integer(my_list=[]):
    y = my_list[0]
    for x in my_list:
        if y < x:
            y = x
    return y
