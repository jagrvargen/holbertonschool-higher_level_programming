#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    contents = dir(hidden_4)
    for item in contents:
        if item[0] != '_':
            print('{}'.format(item))
