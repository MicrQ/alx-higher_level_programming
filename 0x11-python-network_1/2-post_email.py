#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request
    from urllib import parse
    """ Importing necessary modules """

    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('ascii')
    with request.urlopen(argv[1], data=data) as res:
        print(res.read().decode('utf-8'))
