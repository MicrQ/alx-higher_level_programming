#!/usr/bin/python3
""" a python script that fetches 'https://alx-intranet.hbtn.io/status' """

from urllib import request
""" importing the request module """

with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
