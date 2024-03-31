#!/usr/bin/python3
""" sending a request and handling exceptions """

if __name__ == '__main__':
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import HTTPError
    """ necessary modules """

    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
