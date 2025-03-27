#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 > 5:
    print(f"Last digit of %s is %s and is greater than 5", number, number % 10)
