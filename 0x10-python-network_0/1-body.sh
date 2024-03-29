#!/bin/bash
# a script that displays only body of 200 status code after a GET request.
if [ $(curl -sLo /dev/null -w "%{http_code}" "$1") == '200' ]; then curl -sL $1; fi
