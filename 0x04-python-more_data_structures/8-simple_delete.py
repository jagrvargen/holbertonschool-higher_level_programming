#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if my_dict:
        newDict = my_dict
        if key in newDict.keys():
            del newDict[key]
            return newDict
    return my_dict
