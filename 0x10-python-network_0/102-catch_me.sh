#!/bin/bash
# a Bash script that causes the server to respond 'You got me!'
curl -sLX PUT -H "origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
