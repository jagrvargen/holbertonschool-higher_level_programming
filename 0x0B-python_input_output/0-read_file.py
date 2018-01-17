#!/usr/bin/python3


def read_file(filename=""):
    """Reads a text file (utf-8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            print(line.rstrip())
