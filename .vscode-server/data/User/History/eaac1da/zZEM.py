#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print((number) + str('is positive'))
elif number < 0:
    print((number) + str('is negative'))
else:
    print((number) + str('is zero'))