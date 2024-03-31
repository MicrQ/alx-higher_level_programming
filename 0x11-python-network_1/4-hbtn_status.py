#!/usr/bin/python3
""" a script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    import requests
    """ module to fetch the page """

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- {}".format(type(res.text)))
    print("\t- {}".format(res.text))
