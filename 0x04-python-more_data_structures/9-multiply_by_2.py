#!/usr/bin/python3
def multiply_by_2(my_dict):
    if my_dict:
        newDict = dict([(n, v * 2) for n, v in my_dict.items()])
        return newDict
    return my_dict
