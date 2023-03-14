#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    j = 0
    for i in my_list:
        if j == idx:
            if idx < 0:
                return my_list
            else:
                my_list[j] = element
                return my_list
        j += 1
    return my_list
