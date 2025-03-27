#!/usr/bin/python3
import random
a = (65, 90)
b = (97, 122)
Alphabet = random.randint(a)
if Alphabet == a:
    print("{:d} is upper".format(Alphabet))
else:
    print("{:d} is lower".format(Alphabet))
