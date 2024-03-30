#!/usr/bin/python3
""" a python script that takes url argument and displays the 'X-Request-Id'
    of response.
"""

from urllib import request
from sys import argv
""" Importing necessary modules """

with request.urlopen(argv[1]) as res:
    print(res.getheader('X-Request-Id'))
