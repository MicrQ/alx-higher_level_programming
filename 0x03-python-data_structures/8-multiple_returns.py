#!/usr/bin/python3
def multiple_returns(sentence):
    lgz = len(sentence)
    char0 = sentence[0] if lgz > 0 else "None"
    tup = lgz, char0
    return(tup)
