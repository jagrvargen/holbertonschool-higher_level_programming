#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        romanNums = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        numerals = list(roman_string)
        tally = 0
        flag = 0
        for letter in numerals:
            if letter == 'I' and (flag == 0 or flag == 1 or flag == 2):
                flag = 1
            elif letter == 'X' and (flag == 0 or flag == 2 or flag== 3):
                flag = 2
            elif letter == 'C' and (flag == 0 or flag == 3):
                flag = 3
            if flag == 1 and (letter == 'V' or letter == 'X'):
                tally -= 2
                flag = 0
            elif flag == 2 and (letter == 'L' or letter == 'C'):
                tally -= 20
                flag = 0
            elif flag == 3 and (letter == 'D' or letter == 'M'):
                tally -= 200
                flag = 0
            tally += romanNums[letter]
        return tally
    return 0
