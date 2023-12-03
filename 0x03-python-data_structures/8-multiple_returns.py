#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        char0 = None
    else:
        char0 = sentence[0]
    return (len(sentence), char0)
