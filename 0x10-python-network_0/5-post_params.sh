#!/bin/bash
# a Bash script that sends a POST request and displays the body of the response.
curl -sd "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
