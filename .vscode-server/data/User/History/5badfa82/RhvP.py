#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")