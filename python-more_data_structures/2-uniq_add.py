#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_number = set()
    for number in my_list:
        if number in unique_number:
            continue
        else:
            unique_number.add(number)
            result += number
    return result
