#!/bin/bash
# a Bash script that causes the server to respond 'You got me!'
curl -sd "data=You got me!" -X POST 0.0.0.0:5000/catch_me
