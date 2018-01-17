#!/usr/bin/python3


def write_file(filename="", text=""):
    """
       Writes a string to a text file (utf-8) and returns the number of
       characters written.
    """
    word_count = 0
    with open(filename, mode='w', encoding="utf-8") as fp:
        for c in range(len(text)):
            fp.write(text)
            word_count += 1
    return word_count
