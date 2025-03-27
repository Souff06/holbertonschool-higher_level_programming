#!/usr/bin/python3
import random
a = (65, 90)
b = (97, 122)
Alphabet = random.choice(a, b)
if Alphabet == a:
    print("{:d} is upper".format(Alphabet))
elif Alphabet == b:
    print("{:d} is lower".format(Alphabet))
