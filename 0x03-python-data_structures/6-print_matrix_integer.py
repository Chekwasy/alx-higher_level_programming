#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if matrix:
                a = 1
                b = 1
                for i in matrix:
                        c = len(i)
                        for j in i:
                                if a != c:
                                        print("{} ".format(j), end='')
                                else:
                                        print("{}".format(j))
                        print('')
