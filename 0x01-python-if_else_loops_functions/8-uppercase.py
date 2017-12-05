#!/usr/bin/python3
def uppercase(str):
    ### Prints a string in uppercase ###
    for i in range(len(str)):
        c = chr(ord(str[i]))
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
        if i < len(str) - 1:
            print('{}'.format(c), end='')
        else:
            print('{}'.format(c))
