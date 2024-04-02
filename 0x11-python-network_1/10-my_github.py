#!/usr/bin/python3
""" a python script that takes github credentials and displays the user id. """

if __name__ == "__main__":
    import requests
    from sys import argv
    import json
    """ necessary modules """

    res = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2]))
    try:
        print(res.json()['id'])
    except KeyError:
        print(None)
