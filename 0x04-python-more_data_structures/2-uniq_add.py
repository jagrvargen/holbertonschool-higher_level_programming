#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        newList = set(my_list)
        for i in newList:
            result += i
    return result
