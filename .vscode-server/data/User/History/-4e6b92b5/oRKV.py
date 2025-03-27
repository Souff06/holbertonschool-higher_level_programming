#!/usr/bin/python3
import random
a = (65, 90)
b = (97, 122)
ranges = [(65, 90), (97, 122)]
a, b = random.choice(ranges)
Alphabet = random.randint(a, b)
if 65 <= Alphabet <= 90:
    print("{:d} is upper".format(Alphabet))
elif 97 <= Alphabet <= 122:
    print("{:d} is lower".format(Alphabet))
