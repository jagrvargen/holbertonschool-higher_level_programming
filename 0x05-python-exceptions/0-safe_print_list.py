#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for l in range(x):
            print("{}".format(my_list[l]), end="")
            count += 1
    finally:
        print()
        return count
