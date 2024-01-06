#!/bin/bash
# sends JSON POST request to url passed as first arg and diplays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
