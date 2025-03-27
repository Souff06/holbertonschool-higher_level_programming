#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("fizz".format(i), end=" ")
        elif i % 5 == 0:
            print("buzz".format(i), end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz".format(i), end=" ")
        else
            print(i)