#!/usr/bin/python3
""" a script that sends a GET request and
    prints the value of X-Request-Id header.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    """ necessary packages """

    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
