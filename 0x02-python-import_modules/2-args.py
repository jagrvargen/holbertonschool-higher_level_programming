#!/usr/bin/python3
import sys
count = 0
if len(sys.argv) == 2:
    print('1 argument:')
    print('1: {}'.format(sys.argv[1]))
elif len(sys.argv) > 2:
    print('{} arguments:'.format(len(sys.argv)))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
else:
    print('0 arguments.')
