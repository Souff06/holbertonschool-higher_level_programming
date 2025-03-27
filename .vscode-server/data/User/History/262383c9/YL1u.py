#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = set_1 - set_2
    s2 = set_2 - set_1
    result = s1.union(s2)
    return (result)
