#!/usr/bin/python3
""" a script that sends a post request with 'q' variable
    and it value given argument || ""'
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    import json
    """ necessary modules """

    data = argv[1] if len(argv) == 2 else ""
    print(data)
    res = requests.post('http://0.0.0.0:5000/search_user',
                        data={'q': argv[1]})
    try:
        jsn = res.json()
        if len(jsn) < 1:
            print("No result")
        else:
            print("[{}] {}".format(jsn['id'], jsn['name']))
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
