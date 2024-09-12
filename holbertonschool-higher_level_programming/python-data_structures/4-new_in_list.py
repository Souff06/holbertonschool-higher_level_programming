#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]

    # If idx is valid, replace the element
    if 0 <= idx < len(new_list):
        new_list[idx] = element

    # Return the new list (modified or unmodified)
    return new_list
