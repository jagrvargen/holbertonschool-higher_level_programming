#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        shared = list(set_1 & set_2)
        return shared
    elif set_1 or set_2:
        return set()
