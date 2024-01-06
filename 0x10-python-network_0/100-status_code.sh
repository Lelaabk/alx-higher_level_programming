#!/bin/bash
#Sends request to url passed as arg and displays only status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
