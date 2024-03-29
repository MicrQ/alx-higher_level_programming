#!/bin/bash
# a script that displays only body of 200 status code after a GET request.
if [ $(curl -sI GET $1 | head -1 | cut -d ' ' -f2) == 200 ]; then curl -sL $1; fi