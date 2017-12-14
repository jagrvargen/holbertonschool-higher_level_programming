#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        return set_1 ^ set_2
    elif set_1:
        return set_1
    elif set_2:
        return set_2
