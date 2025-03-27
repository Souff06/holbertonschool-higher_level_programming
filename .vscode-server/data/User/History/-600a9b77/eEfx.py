#!/usr/bin/python3

def best_score(a_dictionary):
    a_dictionary.values()
    if a_dictionary == 0:
        return None
    else:
        best_key = max(a_dictionary, key=a_dictionary.get)
