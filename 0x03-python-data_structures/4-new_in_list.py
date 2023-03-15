#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    j = 1
    i = 0
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    for a in my_list:
        if j == idx:
            new_list[j] = element
            return new_list
        j += 1
    return my_list
