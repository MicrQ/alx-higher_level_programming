#!/bin/bash
# a Bash script that causes the server to respond 'You got me!'
curl -s "0.0.0.0:5000/catch_me?data=You got me!"
