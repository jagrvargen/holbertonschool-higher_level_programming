#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) <= len(my_list_2):
        newList = [0 for i in range(len(my_list_1))]
    else:
        newList = [0 for i in range(len(my_list_2))]
    for i in range(list_length):
        try:
            newList[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return newList
