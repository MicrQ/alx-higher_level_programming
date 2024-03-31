#!/usr/bin/python3
""" a script that sends a post request with given email and
    prints the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    """ necessary modules """

    data = {'email': argv[2]}
    res = requests.post(argv[1], data=data)
    print(res.text)
