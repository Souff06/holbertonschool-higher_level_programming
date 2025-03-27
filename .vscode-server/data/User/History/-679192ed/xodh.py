#!/usr/bin/python3
def no_c(my_string):
    i = 0
    for i in my_string:
        if my_string[i] == "c" or my_string[i] == "C":
            return
        print(my_string[i])
