#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    myTup = ()
    while len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)
    while len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
    for i in range(2):
        myTup = myTup + (tuple_a[i] + tuple_b[i],)
    return myTup
