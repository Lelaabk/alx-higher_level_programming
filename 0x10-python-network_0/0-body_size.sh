#!/bin/bash
# Script to display size of body of response
curl -sI | grep -i Content-Length | awk '{print $2}'
