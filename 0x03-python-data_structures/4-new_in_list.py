#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None and 0 <= idx < len(my_list):
        new = []
        for i in range(0, len(my_list)):
            if i is idx:
                new.append(element)
                continue
            new.append(my_list[i])
        return new
    return my_list
