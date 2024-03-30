#!/usr/bin/python3
""" a python script that fetches 'https://alx-intranet.hbtn.io/status' """

from urllib import request
""" importing the request module """

with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    print("Body response:\n\
    \t- type: {}\n\
    \t- content: {}\n\
    \t- utf8 content: {}".format(
        type(body), body, body.decode('utf-8')
    ))
