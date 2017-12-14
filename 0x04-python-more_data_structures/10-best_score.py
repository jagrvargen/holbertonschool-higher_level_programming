#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        maxScore = 0
        for key in my_dict.keys():
            if my_dict[key] > maxScore:
                maxScore = my_dict[key]
                winner = key
        return key
