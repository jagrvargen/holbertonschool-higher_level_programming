#!/usr/bin/python3
# An algorithm to find a peak in a list of unsorted integers.


def find_peak(list_of_integers):
    start = 0
    end = len(list_of_integers) - 1

    if start == end:
        return list_of_integers[0]

    while start <= end:
        if list_of_integers[start] > list_of_integers[start + 1]:
            return list_of_integers[start]
        elif list_of_integers[end] > list_of_integers[end - 1]:
            return list_of_integers[end]
        start += 1
        end -= 1

    return list_of_integers[start]
