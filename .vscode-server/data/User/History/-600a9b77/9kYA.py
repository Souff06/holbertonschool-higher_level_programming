#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

# Test avec l'exemple donné
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Meilleure note: {}".format(best_key))

best_key = best_score(None)
print("Meilleure note: {}".format(best_key))
