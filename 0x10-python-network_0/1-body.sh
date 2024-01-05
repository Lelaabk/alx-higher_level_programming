#!/bin/bash
# Script to display body of response for 200 status code

curl -sL -w "%{http_code}" "$1" -o /dev/null | {
	read -r status
	if [[ $status -eq 200 ]]; then
		curl -s "$1"
	fi
}
