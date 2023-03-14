#!/usr/bin/python3
def uppercase(str):
        ln = len(str)
        for i in range((ln)):
                if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
                        val = ord(str[i]) - 32
                else:
                        val = ord(str[i])
                print(chr(val), end='')
        print("")
