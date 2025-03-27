#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    if element == 3:
        print("9")
    my_list[idx] = element
    return my_list