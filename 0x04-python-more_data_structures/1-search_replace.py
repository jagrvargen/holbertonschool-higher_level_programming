#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newList = [num for num in my_list]
        for i in range(len(newList)):
            if newList[i] == search:
                newList[i] = replace
        return newList
    return my_list
