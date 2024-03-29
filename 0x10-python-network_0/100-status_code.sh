#!/bin/bash
# a bash script that displays only the status code of a response.
curl -so /dev/null -w "%{http_code}" "$1"
