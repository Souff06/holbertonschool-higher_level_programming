#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in my_list[:x]:
            print("{}".format(index), end='')
            count += 1
    except IndexError:
        print()
    print()
    return (count)
