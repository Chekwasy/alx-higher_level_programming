#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for i in my_string:
        if ord(i) != 99 and ord(i) != (99 - 32):
            new_str += i
    return new_str
