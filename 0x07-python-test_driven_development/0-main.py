#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer((9, 9), 2))
print(add_integer(100, -2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
