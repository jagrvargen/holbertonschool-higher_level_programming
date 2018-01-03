#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0

        for l in range(x):
            if type(my_list[l]) == int:
                print("{:d}".format(my_list[l]), end="")
                count += 1
        print()
        return count
    except (TypeError, ValueError):
        pass
