#!/usr/bin/python3
for l in range(122, 96, -1):
    if l % 2 == 1:
        l -= 32
    print(chr(l), end='')
