#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    j = 1
    i = 0
    new_list = []
    if idx < 0:
        return my_list
    for b in my_list:
        new_list.append(my_list[i])
        i += 1
    for a in my_list:
        if j == idx:
            new_list[j] = element
            return new_list
        j += 1
    return my_list
