#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("Fizz ".format(i), end="")
        elif i % 5 == 0:
            print("Buzz ".format(i), end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ".format(i), end="")
        else:
            print(i)
    print("Buzz")
