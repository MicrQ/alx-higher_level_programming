#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_score = list(a_dictionary)[0]
    max_value = a_dictionary[max_score]
    for i in a_dictionary:
        if (a_dictionary[i] > max_value):
            max_score = i
    return (max_score)
