#!/bin/bash
# a bash script that sends JSON POST request.
curl -sd "@$2" -H "Content-Type: application/json" -X POST "$1"
