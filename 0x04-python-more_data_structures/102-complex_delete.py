#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cp_dict = a_dictionary
    if value in list(cp_dict.values()):
        for key in list(cp_dict.keys()):
            if cp_dict.get(key) == value:
                del cp_dict[key]
    return (cp_dict)
