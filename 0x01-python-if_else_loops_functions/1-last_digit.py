#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = 0
if number < 0:
        n = number * (-1)
        number = n

num = number % 10

if n != 0:
        number = number * (-1)
        num = num * (-1)

if num > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
        print("Last digit of {} is {} and is 0".format(number, num))
elif num < 6:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, num))
