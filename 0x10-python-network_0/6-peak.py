#!/usr/bin/python3
""" a function that finds a peak in a given array """


def find_peak(list_of_integers):
    """ finds a peak in a list """
    left = 0
    right = len(list_of_integers) - 1
    if list_of_integers is None or len(list_of_integers) < 1:
        return None
    if len(list_of_integers) == 1 or (
            list_of_integers[0] >= list_of_integers[1]):
        return list_of_integers[0]
    if list_of_integers[right] >= list_of_integers[right - 1]:
        return list_of_integers[right]

    while (left < right):
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
