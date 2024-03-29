#!/bin/bash
# a bash script that lists all HTTP methods the server will accept.
curl -sI GET "$1" | grep 'Allow:' | cut -d ' ' -f2
