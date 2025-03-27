#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    while x < len(my_list):
    try:
        print(x)
    except OutElement:
        print()