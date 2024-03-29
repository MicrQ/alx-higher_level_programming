#!/bin/bash
# a bash script that sends a GET request and sends X-School-User-Id=98.
curl -sH "X-School-User-Id: 98" "$1"
