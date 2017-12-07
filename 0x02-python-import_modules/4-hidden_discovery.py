#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    contents = dir(hidden_4)
    for item in contents:
        if item[0] != '_':
            print('{}'.format(item))
