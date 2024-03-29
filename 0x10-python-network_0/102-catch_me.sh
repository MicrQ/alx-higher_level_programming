#!/bin/bash
# a Bash script that causes the server to respond 'You got me!'
curl -sX POST -H "User-Agent: You got me!" -H "Accept: text/plain" 0.0.0.0:5000/catch_me
