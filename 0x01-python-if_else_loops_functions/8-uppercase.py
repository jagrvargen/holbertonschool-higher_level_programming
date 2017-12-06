#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = c - 32
        if i < len(str):
            print('{}'.format(chr(c)), end='')
    print('')
