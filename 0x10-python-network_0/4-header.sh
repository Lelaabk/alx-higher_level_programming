#!/bin/bash
# Takes url and sends a GET request with specific header and displays body of response
curl -sH "X-School-User-Id:98" "$1"
