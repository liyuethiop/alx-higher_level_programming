#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for y in new:
        if y == search:
            idx = new.index(y)
            new[idx] = replace
    return new
