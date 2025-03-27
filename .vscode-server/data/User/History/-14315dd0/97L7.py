#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    while x < max(my_list[x]):
        print(x)
    try:
        print(x)
    except OutElement:
        return None
