#!/bin/bash
# Script to display body of response for 200 status code
curl -sX GET "$1" -L 200
