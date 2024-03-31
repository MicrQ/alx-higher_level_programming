#!/usr/bin/python3
""" a script that sends a get request and displays the response.
    if the status code is <= 400, the script will print 'Error code:'
    followed by the status code.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    """ necessary modules """

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
